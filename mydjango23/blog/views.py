from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import PostForm
from blog.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    post_qs = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list': post_qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {
        "post": post,
    })


def post_new(request: HttpRequest) -> HttpResponse:
    # request.method  # "GET", "POST"

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            messages.success(request, "새로운 포스팅을 저장했습니다.")
            return redirect("blog:post_detail", saved_post.pk)
    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {
        "form": form,
    })


def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            saved_post = form.save()
            messages.success(request, f"#{pk} 포스팅을 저장했습니다.")
            return redirect("blog:post_detail", saved_post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {
        "form": form,
        "post": post,
    })


def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    raise NotImplementedError("삭제는 아직 강의에서 다루지 않았습니다.")
