from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated(), IsCustomer()]
        return [permissions.IsAuthenticated(), IsManager()]

    def perform_create(self, serializer):
        serializer.save()

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated(), IsCustomer()]
        return [permissions.IsAuthenticated(), IsManager()]

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'manager'

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'customer'
