from django.contrib import admin
from shop.models import Shop, Review, Tag


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
