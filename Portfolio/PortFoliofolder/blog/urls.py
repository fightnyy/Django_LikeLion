
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import blog.views

urlpatterns = [
    path('<int:blog_id>',blog.views.detail,name="detail"),
    path('new/',blog.views.new,name="new"),
    path('blog/create',blog.views.create,name="create"),
]