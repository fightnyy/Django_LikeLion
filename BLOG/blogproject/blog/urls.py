from django.contrib import admin
from django.urls import path
import blogapp.views
urlpatterns = [
    path('', blogapp.views.home, name="home"),
    path('admin/', admin.site.urls),
    # 위 내용은 주소를 "blog/int값" 이런형식으로 값을 받겠다는 의미이다.
    path('blog/<int:blog_id>', blogapp.views.detail, name="detail"),
    # 꺽쇠 안에 있는 건 path convertor 라고 불린다. 숫자로 계층적인 url을 자동적으로 형상화 할수 있게 만들어 주는 요소이다.
    # 여기서 int는 1,2,3,4,5이렇게 되는거고 blog_id는 detail에 넘어가는 요소이다.인자를 넘겨준다.
]
