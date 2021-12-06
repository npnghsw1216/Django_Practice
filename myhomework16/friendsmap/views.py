from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from friendsmap.models import Post


def map_list(request: HttpRequest) -> HttpResponse:
    # request.GET  # QueryString Values
    # request.POST  # Post 요청 Values
    # request.FILES  # Post 요청에서 파일 Values

    qs = Post.objects.all()  # QuerySet Type
    qs = qs.order_by("-pk")

    query = request.GET.get("query", "")

    if query:
        qs = qs.filter(title__icontains=query)

    context_data = {
        "map_list": qs,
    }

    # blog/templates/blog/post_list.html
    return render(request, "friendsmap/map_list.html", context_data)


def map_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # pk=1

    post = Post.objects.get(pk=pk)  # id=pk
    return render(request, "friendsmap/map_detail.html", {
        "post": post,
    })
