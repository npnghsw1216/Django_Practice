from django.contrib import admin


from delicious.models import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "latitude", "longitude", "telephone"]
    list_display_links = ["name"]

admin.site.register(Shop, ShopAdmin) #등록