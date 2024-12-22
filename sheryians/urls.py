from django.urls import path
from .views import *
app_name='sheryians'

urlpatterns = [
    path('',home,name='home'),
    path('course/',course,name='course'),
    path('video2',video2,name='video2'),
    path('video3',video3,name='video3'),
    path('video4',video4,name='video4'),
    path('video5',video5,name='video5'),
    path('bootcamp',bootcamp,name='bootcamp'),
]