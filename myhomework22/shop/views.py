from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from shop.form import ShopForm
from shop.models import Shop, Category


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()

    category_id: str = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__pk=category_id)

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)

    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
        "category_list": qs,
    })


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)

    return render(request, "shop/shop_detail.html", {
        "shop": shop,
    })


def shop_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()

            return redirect("shop:shop_detail", saved_post.pk)
    else:
        form = ShopForm()
    return render(request, "shop/shop_form.html", {
        "form": form,
    })


def shop_edit(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            saved_shop = form.save()
            return redirect("shop:shop_detail", saved_shop.pk)
    else:
        form = ShopForm(instance=shop)

    return render(request, "shop/shop_form.html", {
        "form": form,
    })
