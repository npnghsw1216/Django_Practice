from django import forms
from shop.models import Shop, Review


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
