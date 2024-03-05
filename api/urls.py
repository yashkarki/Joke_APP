from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path('get_new_joke/', get_new_joke, name='get_new_joke'),
]
