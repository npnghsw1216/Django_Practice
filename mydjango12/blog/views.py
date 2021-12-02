from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from blog.models import Post


def index(request):
    return render(request, "blog/index.html")


def post_list(request: HttpRequest) -> HttpResponse:
    # request.GET  # QueryString Values
    # request.POST  # Post 요청 Values
    # request.FILES  # Post 요청에서 파일 Values

    qs = Post.objects.all()  # QuerySet Type
    qs = qs.order_by("-pk")

    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(title__icontains=q)


    # blog/templates/blog/post_list.html
    return render(request, "blog/post_list.html", {
        "post_list": qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # pk=1

    post = Post.objects.get(pk=pk)  # id=pk
    return render(request, "blog/post_detail.html",{
        "post": post,
    })

