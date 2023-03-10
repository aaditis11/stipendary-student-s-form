from app import views
from django.urls import include, path

urlpatterns = [
    path('',views.login, name='login'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('form',views.form, name='form'),
]