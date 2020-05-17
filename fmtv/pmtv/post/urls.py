from django.urls import path
import post.views

urlpatterns = [
    path('', post.views.post_list, name = 'post_list'), 
    #''(공백) url이 들어오면 post_list 함수를 호출한다
]