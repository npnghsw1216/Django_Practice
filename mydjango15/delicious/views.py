from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from delicious.forms import ShopForm
from delicious.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()

    # QueryString에 query 이름의 인자를 확인
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    # template_name = "delicious/shop_list.html"
    template_name = "delicious/shop_list.html"
    context_data = {
        "shop_list": qs,
    }
    return render(request, "delicious/shop_list.html", context_data)


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = Shop.objects.get(pk=pk)
    template_name = "delicious/shop_detail.html"
    context_data = {
        "shop": shop,
    }
    return render(request, "delicious/shop_detail.html", context_data)


def shop_new_1(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "delicious/shop_form_1.html", {})
    else:
        name = request.POST["name"]
        description = request.POST["description"]
        address = request.POST["address"]
        latitude = request.POST["latitude"]
        longitude = request.POST["longitude"]
        telephone = request.POST["telephone"]
        # TODO: 유효성 검사:...
        Shop.objects.create(
            name=name,
            description=description,
            address=address,
            latitude=latitude,
            longitude=longitude,
            telephone=telephone,
        )
        return redirect("/delicious/")


shop_new = CreateView.as_view(
    model=Shop,
    form_class=ShopForm,
    success_url="/delicious/",
)