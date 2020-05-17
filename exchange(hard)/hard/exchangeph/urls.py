from django.contrib import admin
from django.urls import path
import exchangeapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',exchangeapp.views.home,name='home'),#django templates 에서 url 함수를 이용할 때 쓰는 것
    path('result/',exchangeapp.views.result,name='result'),
    path('about/',exchangeapp.views.about,name='about'),
]
