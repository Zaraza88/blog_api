from django.urls import path

from .import views


urlpatterns = [
    path('register/', views.RegistrUserView.as_view(), name='registr'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('login/', views.LoginGenericAPIView.as_view(), name='login'),
]
