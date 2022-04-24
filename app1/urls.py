import imp
from turtle import home
from django.urls import path
from .views import Home, Login, Register, Profile, Logout


urlpatterns =[
    path('', Home.as_view(), name='HOME'),
    path('login/', Login.as_view(), name='LOGIN'),
    path('register/', Register.as_view(), name='REGISTER'),
    path('profile/', Profile.as_view(), name='PROFILE'),
    path('logout/', Logout.as_view(), name='LOGOUT')
]