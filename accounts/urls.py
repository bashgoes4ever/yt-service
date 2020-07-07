# coding=utf-8
from django.urls import path
from .views import *


urlpatterns = [
    path('users/login', UserLogin.as_view()),
    path('users/<int:id>', Users.as_view()),
    path('users/<int:id>/orders', AccountOrders.as_view()),
    path('users/', Users.as_view()),
    path('sites/', Sites.as_view()),
    path('amount/', UserAmount.as_view()),
    path('amount/<int:id>', ChangeAccountAmount.as_view()),
]