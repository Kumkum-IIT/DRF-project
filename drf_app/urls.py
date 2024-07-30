from django.urls import path
from .views import *
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import include

urlpatterns = [
    path('',views.index_view,name='index'),
    path('register/', views.RegisterViewSet.as_view({'post': 'create'}), name='register'),
    path('login/', views.LoginViewSet.as_view({'post': 'create'}), name='login'),
    path('users/<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve'}), name='users'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
