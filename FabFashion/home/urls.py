from django.urls import path
from .views import homeView,loginView,registerView

urlpatterns = [
   
    path('',homeView,name='home'),
    path('register/',registerView,name='register'),
    path('login/',loginView,name='login'),
]