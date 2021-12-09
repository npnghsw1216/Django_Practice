from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from diary.forms import PostForm
from diary.models import Post


def tag_detail(request: HttpRequest, tag_name: str) -> HttpResponse:
    qs = Post.objects.all()
    qs = qs.filter(tag_set__name=tag_name)

    return render(request, "diary/tag_detail.html",{
        "tag_name": tag_name,
        "post_list": qs,
    })


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)

    return render(request, "diary/post_list.html", {
        "post_list": qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    comment_list = post.comment_set.all()
    tag_list = post.tag_set.all()
    return render(request, "diary/post_detail.html", {
        "post": post,
        "comment_list": comment_list,
        "tag_list": tag_list,
    })


def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # ModelForm에서만 지원
            post.ip = request.META["REMOTE_ADDR"]
            post.save()  # ModelForm에서만 지원
            messages.success(request, "성공적으로 저장했습니다.")
            return redirect("diary:post_list")
    else:
        form = PostForm()

    return render(request, "diary/post_form.html", {
        "form": form,
    })


def post_edit(request: HttpRequest, pk:int) -> HttpResponse:
    # 아래 코드는 ModelForm에 한해서 동작하는 코드.
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "성공적으로 저장했습니다.")
            return redirect("diary:post_list")
    else:
        form = PostForm(instance=post)

    return render(request, "diary/post_form.html", {
        "form": form,
    })
