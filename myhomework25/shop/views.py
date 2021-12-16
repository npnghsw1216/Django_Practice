from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

from shop.forms import ShopForm
from shop.models import Shop

shop_list = ListView.as_view(
    model=Shop,
)

shop_detail = DetailView.as_view(
    model=Shop,
)


class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm

    def get_success_url(self):
        shop_pk = self.object.pk
        return reverse("shop:shop_detail", args=[shop_pk])


shop_new = ShopCreateView.as_view()