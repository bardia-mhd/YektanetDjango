from django.contrib import admin
from .models import Ad, Advertiser


class AdminAdModel(admin.ModelAdmin):
    list_display = ('title', 'approve')
    list_filter = ('approve', 'advertiser')
    search_fields = ('title',)


class AdminAdvertiserModel(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Ad, AdminAdModel)
admin.site.register(Advertiser, AdminAdvertiserModel)
