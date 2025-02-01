from django.urls import path
from .views import UserRegistrationView, UserListView, UserDetailView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', UserLoginView.as_view(), name='login'),
]
