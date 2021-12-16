from django.contrib import admin

from shop.models import Category, Shop, Review, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    pass

