from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from constellation.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()

    query = request.GET.get("query", "")

    if query:
        qs = qs.filter(title__icontains=query)

    return render(request, "constellation/post_list.html", {
        "post_list": qs,
    })


def post_detail(request: HttpRequest, pk=int) -> HttpResponse:
    post = Post.objects.get(pk=pk)

    return render(request, "constellation/post_detail.html", {
        "post": post,
    })
