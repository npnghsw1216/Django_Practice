from shop.forms import ShopForm
from shop.models import Shop
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

shop_list = ListView.as_view(
    model=Shop,
)

shop_detail = DetailView.as_view(
    model=Shop,
)


class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm
    template_name = 'shop/shop_form.html'

    def get_success_url(self):
        post_pk = self.object.pk
        return reverse("shop:shop_detail", args=[post_pk])


shop_new = ShopCreateView.as_view()


class ShopUpdateView(UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = 'shop/shop_form.html'


shop_edit = ShopUpdateView.as_view()

post_delete = DeleteView.as_view(
    model=Shop,
    success_url=reverse_lazy("shop:shop_list")
)
