from django.shortcuts import render, get_object_or_404
from blogapp.models import Blog
# Create your views here.


def home(request):
    blogs = Blog.objects  # 쿼리셋
    return render(request, 'home.html', {'blogs': blogs})

# Usaully When we use Queryset and method Formats are already defined. (i.e. QuerySet Blog.objects, methond Queryset.method


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'blog_detail': blog_detail})

# get_object_or_404:object를 가져와 주기도 하고(get_object)예외처리(or_404)도 해주는 역할
