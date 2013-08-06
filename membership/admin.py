from django.contrib import admin
from membership.models import Shop, Member

class ShopAdmin(admin.ModelAdmin):
    fields = ['name', 'city']
    list_display = ('name', 'city')

admin.site.register(Shop, ShopAdmin)
admin.site.register(Member)
