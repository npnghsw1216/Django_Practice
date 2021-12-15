from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from shop.forms import ShopForm, ReviewForm
from shop.models import Shop, Review


def tag_detail(request: HttpRequest, tag_name: str) -> HttpResponse:
    qs = Shop.objects.all()
    qs = qs.filter(tag_set__name=tag_name)

    return render(request, "shop/tag_detail.html", {
        "tag_name": tag_name,
        "shop_list": qs,
    })


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
    })


# /shop/100/
def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    review_list = shop.review_set.all()
    tag_list = shop.tag_set.all()

    return render(request, "shop/shop_detail.html", {
        "shop": shop,
        "review_list": review_list,
        "tag_list": tag_list,
    })


# /shop/new/
def shop_new(request: HttpRequest) -> HttpResponse:
    # raise NotImplementedError("구현 예정")
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.save()
            messages.success(request, "성공적으로 저장했습니다.")
            return redirect("shop:shop_list")
    else:
        form = ShopForm()

    return render(request, "shop/shop_form.html", {
        "form": form,
    })


def shop_edit(request: HttpRequest, pk: int) -> HttpResponse:
    # 아래 코드는 ModelForm 에 한해서 동작하는 코드.
    shop = get_object_or_404(Shop, pk=pk)

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            form.save()
            messages.success(request, "성공적으로 저장했습니다.")
            return redirect("shop:shop_list")
    else:
        form = ShopForm(instance=shop)

    return render(request, "shop/shop_form.html", {
        "form": form,
    })


def review_new(request: HttpRequest, shop_pk: int) -> HttpResponse:

    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            # form.cleaned_data  # 유효성 검사에 통과한 값들 (dict)
            review = form.save(commit=False)
            review.shop = shop
            review.save()
            return redirect("shop:shop_detail", shop_pk)

    else:
        form = ReviewForm()
    return render(request, "shop/review_form.html", {
        "form": form,

    })


def review_edit(request: HttpRequest, shop_pk, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect("shop:shop_detail", shop_pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, "shop/review_form.html", {
        "form": form,
    })
