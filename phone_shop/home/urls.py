from django.urls import path
from .views import *
from home.views import*
from . import views
urlpatterns = [
    path('', views.home, name='home'),
]