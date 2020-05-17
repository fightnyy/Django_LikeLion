
from django.contrib import admin
from django.urls import path
import wordcounter.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wordcounter.views.home,name="home"),
    path('about/',wordcounter.views.about,name="about"),
    path('counter/',wordcounter.views.counter,name="counter")
]
