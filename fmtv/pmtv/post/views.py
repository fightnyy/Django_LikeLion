from django.shortcuts import render
from post.models import Post    # post모델 임포트

# Create your views here.

def post_list(request):

    post_list = Post.objects.all()  # Post 모델에있는 객체 다 가져와

    return render(request, 'post.html', {'post_list' : post_list})  # 변수 넘겨줘