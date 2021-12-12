from django import forms
from shop.models import Shop, Review


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            "name",
            "description",
            "telephone",
            "photo",
            "tag_set",
        ]


class ReviewForm(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = Review
        fields = ["shop", "name", "message"]
