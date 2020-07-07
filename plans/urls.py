# coding=utf-8
from django.urls import path
from .views import *


urlpatterns = [
    path('plans/custom/', CustomPrices.as_view()),
    path('plans/custom/<int:id>', CustomPrices.as_view()),
    path('plans/', Plans.as_view()),
    path('plans/<int:id>', Plans.as_view()),
    path('client/plans/', PlansClient.as_view()),
]