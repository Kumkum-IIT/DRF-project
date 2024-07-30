from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializers  # Make sure this serializer is correctly defined in your serializers.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_app.serializers import UserSerializers,LoginSerializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .permissions import IsSuperUser 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import render


class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response({'message': 'Login successful', 'token': token})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

    

class RegisterViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]

    def create(self, request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Generate JWT token for the user
        refresh = RefreshToken.for_user(user)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response({'message': 'User created successfully', 'token': token})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  # Apply the custom permission

    def retrieve(self, request, *args, **kwargs):
        user = request.user  # Get the user from the request (from JWT token)
        instance = self.get_object()

        if user != instance:
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

def index_view(request):
    if request=='GET':
        return render(request, 'index.html')
    return render(request, 'index.html')
