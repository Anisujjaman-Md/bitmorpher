from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/users/<str:username>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
]
