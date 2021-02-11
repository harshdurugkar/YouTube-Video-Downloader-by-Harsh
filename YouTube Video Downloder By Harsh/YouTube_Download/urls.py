from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ytd_home, name='home'),
    path('ytdownload/', views.yt_download),
    path('download_complete/<resolutions>/', views.download_complete, name='download_completedd')
]
