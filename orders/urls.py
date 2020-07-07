# coding=utf-8
from django.urls import path
from .views import *


urlpatterns = [
    path('orders/', Orders.as_view()),
    path('orders/<int:id>', Orders.as_view()),
    path('orders/statuses', Statuses.as_view()),
    path('client/orders/', OrdersClient.as_view()),
    path('client/price/', CalculatePrice.as_view()),
]