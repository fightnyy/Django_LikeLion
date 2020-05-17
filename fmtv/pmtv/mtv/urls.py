from django.contrib import admin
from django.urls import path,include
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.index,name='home'),
    path('lions/', myapp.views.list_lion,name='lions'),
    # url에 'lions/'이 입력되면 myapp/views.py에 있는 lion_list 함수를 호출해준다
    path('post/', include('post.urls')), 
    path('lions/<int:pk>', myapp.views.lion_posts, name='lion_posts'), # 추가
    # post.urls를 include 해주는데 처음 url이 `post/` 가 된다  
]
