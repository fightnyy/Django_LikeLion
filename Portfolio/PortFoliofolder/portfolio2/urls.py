from django.contrib import admin
from django.urls import path,include
import portfolio2.views

urlpatterns = [
    path('',portfolio2.views.portfolio,name="portfolio"),
]
