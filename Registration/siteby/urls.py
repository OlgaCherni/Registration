from django.contrib import admin
from django.urls import path
from pril.views import index, main
from pril2.views import about, time


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("main/", main, name='main'),
    path("about/", about, name="about"),
    path("time/", time, name='date'),         
]

 