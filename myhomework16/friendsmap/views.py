from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from friendsmap.models import Post


def map_list(request: HttpRequest) -> HttpResponse:

    qs = Post.objects.all()  # QuerySet Type
    qs = qs.order_by("-pk")

    return render(request, "friendsmap/map_list.html")


def map_detail(request: HttpRequest, pk=int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    return render(request, "friendsmap/map_detail.html", {
        "post": post,
    })