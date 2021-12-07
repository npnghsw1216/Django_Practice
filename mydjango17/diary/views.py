from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from diary.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, "diary/post_list.html", {
        "post_list": qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    return render(request, "diary/post_detail.html", {
        "post": post,
    })