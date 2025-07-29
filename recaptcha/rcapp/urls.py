from django.urls import path,include
from .views import *
urlpatterns = [

    path('', register),
    path('index',home),
    path('success/',success),
    path('dashboard/',dashboard)
]