from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.contrib.auth import get_user_model

# Create your views here.
class UserAPIView(APIView):

    def get(self, request):

        users = get_user_model().objects.all()

        serializer = UserSerializer(users, many = True)

        return Response(data= serializer.data, status = status.HTTP_200_OK)

    def post(self, request):

        serializer = UserSerializer(data = request.data)

        try:

            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(data= f"Item guardado con exito.{serializer.data}", status = status.HTTP_201_CREATED)

        except IntegrityError:

            return Response(data="Error al guardar en base de datos", status=status.HTTP_500_INTERNAL_SERVER_ERROR)