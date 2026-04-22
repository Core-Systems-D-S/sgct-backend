from django.shortcuts import render
from rest_framework. views import APIView
from .serializer import GroupSerializer
from django.db import IntegrityError, transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserGroup
# Create your views here.
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
        