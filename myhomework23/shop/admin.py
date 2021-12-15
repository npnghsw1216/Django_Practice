from django.contrib import admin
from shop.models import Category, Shop, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
