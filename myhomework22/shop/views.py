from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from shop.models import Shop, Category


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    category_qs = Category.objects.all()
    category_id:str = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__pk=category_id)

    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
        "category_list": category_qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)

    return render(request, "shop/shop_detail.html", {
        "shop": shop,
    })
