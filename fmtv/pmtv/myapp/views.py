from django.shortcuts import render
from myapp.models import Lion
from post.models import Post
def index (request):
    return render(request,'index.html')


def list_lion(request):
    lion_list=Lion.objects.all()
    return render(request,'lions.html',{'lion_list':lion_list})

def lion_posts(request, pk): # pk 를 받아서 처리해주니 인자에 pk를 추가해주고
    
    post_pk = pk                                # post_pk 에 넘겨받은 pk를 저장
    author = Lion.objects.get(pk = post_pk)     # 작성자를 Lion model의 해당 pk를 가진 사람 가져와
    post_list = Post.objects.all().filter(name = author)
    # 게시글을 Post model의 해당 작성자를 가진 게시물들 가져와
    
    return render(request, 'lion_posts.html', { # 만든 변수들 넘겨주기
        'post_list' : post_list,
        'author' : author,
        'post_pk' : pk,
        })