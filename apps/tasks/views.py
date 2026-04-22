from rest_framework.views import APIView
from .serializers import TaskSerializer, TaskComentSerializer
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status
from .models import Task

class TaskAPIView(APIView):

    def post (self, request):

        serializer = TaskSerializer(data = request.data, context = {"request" : request})

        serializer.is_valid(raise_exception = True)

        try:
            serializer.save(created_by = request.user, )
            return Response(data= F"Tarea creada con éxito:{serializer.data['title']}")
        
        except IntegrityError:
            return Response(data= "Ocurrió un error en base de datos", status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):

        task = Task.object.all()

        serializer = TaskSerializer(task, many = True)

        return Response(data = serializer.data, status = status.HTTP_200_OK)

class TaskCommentAPIView(APIView):

    def post(self, request):
        
        serializer = TaskComentSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        try:

            serializer.save(user=request.user)

            return Response(data =f"Comentario creado: {serializer.data["content"]}", status=status.HTTP_201_CREATED)
        
        except IntegrityError as e:

            return Response(data= "Error al crear el comentario", status=status.HTTP_500_INTERNAL_SERVER_ERROR)