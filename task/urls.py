from django.contrib import admin
from django.urls import path,include
from .views import FetchDetails


urlpatterns = [
    path('fetch/',FetchDetails.as_view(),name='fetch'),
]
