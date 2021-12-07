from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from news.models import Post


def tag_detail(request: HttpRequest, tag_name: str) -> HttpResponse:
    qs = Post.objects.all()
    qs = qs.filter(tag_set__name=tag_name)


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()

    return render(request, "news/post_list.html", {
        "tag_name": tag_name,
        "post_list: qs"
    })


def post_detail(request: HttpRequest, pk=int) -> HttpResponse:
    post = Post.objects.get(pk=pk)

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)
    return render(request, "news/post_detail.html",{
        "post": post,
    })


