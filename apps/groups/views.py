#importaciones de la biblioteca estandar

#Importaciones de terceros
from django.shortcuts import render, get_object_or_404
from django.db import IntegrityError, transaction
from rest_framework. views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
#Importaciones de mi app
from .models import Group, UserGroup

from .serializer import GroupSerializer

class GroupAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = GroupSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        try:
            
            with transaction.atomic():

                group = serializer.save(owner= request.user)

                UserGroup.objects.create(
                    user = request.user,
                    group = group,
                    role = 'admin'
                )

                return Response(data = GroupSerializer(group).data, status=status.HTTP_201_CREATED)
        
        except IntegrityError:

            return Response("Hubo un problema con la base de datos.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request, pk=None):
        if pk:
            data = get_object_or_404(Group, id = pk)
            serializer = GroupSerializer(data)
        else:
            data = Group.objects.all()
            serializer = GroupSerializer(data, many = True)

        return Response(data= serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk):

        existed = get_object_or_404(Group, id=pk)

        serializer = GroupSerializer(existed, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=f"Se ha actualizado el registro {serializer.data.get('name')}", status=status.HTTP_200_OK)
        
        return  Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        group = get_object_or_404(Group, id = pk)

        group.delete()

        return Response(f"Se eliminó con exito el grupo con id {pk}", status = status.HTTP_200_OK)
        
