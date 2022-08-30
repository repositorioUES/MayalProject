from django.urls import path
from .views import *

urlpatterns = [
    path('administrador', index, name="index"),


]