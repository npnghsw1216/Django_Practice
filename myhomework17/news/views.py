from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from news.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()

    return render(request, "news/post_list.html",{
        "post_list: qs"
    })


def post_detail(request: HttpRequest, pk=int) -> HttpResponse:
    post = Post.objects.get(pk=pk)

    return render(request, "news/post_detail.html",{
        "post":post,
    })


