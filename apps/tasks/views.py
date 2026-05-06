from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import TaskSerializer, TaskComentSerializer
from .models import Task

class TaskAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post (self, request):

        serializer = TaskSerializer(data = request.data, context = {"request" : request})

        serializer.is_valid(raise_exception = True)

        try:
            serializer.save(created_by = request.user)
            return Response(data= F"Tarea creada con éxito: {serializer.data['title']}")
        
        except IntegrityError:
            return Response(data= "Ocurrió un error en base de datos", status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):

        task = Task.objects.all()

        serializer = TaskSerializer(task, many = True)

        return Response(data = serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk):

        task = get_object_or_404(Task, id=pk)

        serializer = TaskSerializer(task, data=request.data, context = {"request" : request})

        if serializer.is_valid():

            serializer.save()
            
            return Response(data= "Tarea actualizada correctamente", status = status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        task = get_object_or_404(Task, id = pk)
        task.delete()
        return Response(data="Objeto eliminado satisfactoriamente", status = status.HTTP_200_OK)
        
class TaskCommentAPIView(APIView):

    def post(self, request):
        
        serializer = TaskComentSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        try:

            serializer.save(user=request.user)

            return Response(data =f"Comentario creado: {serializer.data["content"]}", status=status.HTTP_201_CREATED)
        
        except IntegrityError as e:

            return Response(data= "Error al crear el comentario", status=status.HTTP_500_INTERNAL_SERVER_ERROR)