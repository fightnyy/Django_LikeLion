"""exchangeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import exchangeapp.views
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',exchangeapp.views.home,name='home'),#여기서의 name의 의미는 url 쓰고 이후에 'home'을 쓰면 바로 2번째 매개변수에 있는 값이 실행된다.라는 의미이다
    path('usd/',exchangeapp.views.usd,name='usd'),
    path('jpy/',exchangeapp.views.jpy,name='jpy'),
    path('can/',exchangeapp.views.can,name='can'),

]
