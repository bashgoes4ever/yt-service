# coding=utf-8
from django.urls import path
from .views import *


urlpatterns = [
    path('logs/', Logs.as_view()),
    path('logs/<int:id>', Logs.as_view()),
]