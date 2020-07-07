# coding=utf-8
from django.urls import path
from .views import *


urlpatterns = [
    path('news', Articles.as_view()),
    path('news/<int:id>', Articles.as_view()),
    path('client/news', Articles.as_view()),
    path('client/news/<int:id>', Articles.as_view()),
]

