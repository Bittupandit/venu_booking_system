# from django.contrib import admin
from django.urls import path
# from django.urls.conf import include
from .views import *
urlpatterns = [
    path('',home_page,name='home-page'),
    path('detail/<int:pk>/',detail_page,name='detail-page'),
]