from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView

from delicious.forms import ShopForm
from delicious.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()

    # Querystring 에 query 이름의 인자를 확인
    query = request.GET.get("query", "")    # query 값을 가져오는데 없다면 빈 문자열을 가져와라
    if query:
        qs = qs.filter(name__icontains=query)

    # templates_name = "delicious/shop_list.html"
    context_data = {
        "shop_list":qs,
    }
    return render(request, "delicious/shop_list.html", context_data)

def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = Shop.objects.get(pk=pk)   # pk(필드 값)=pk(변수명), # .get은 하나만 찾는다
    # template_name = "delicious/shop_detail.html"
    context_data = {
        "shop": shop,   # "Shop"(Shop으로 지정): shop(변수명, 큰 의미 x)
    }   # 템플릿에서 보여주는 값들
    return render(request, "delicious/shop_detail.html", context_data)


def shop_new_1(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":   # "GET", "POST"
        return render(request, "delicious/shop_form_1.html", {})
    else:   # POST
        name = request.POST["name"]
        description = request.POST["description"]
        address = request.POST["address"]
        latitude = request.POST["latitude"]
        longitude = request.POST["longitude"]
        telephone = request.POST["telephone"]
        # TODO: 유효성 검사...(원래는 검사를 진행해야 한다.)
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
    success_url="/delicious/"
)