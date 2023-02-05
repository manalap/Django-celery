from django.contrib import admin
from django.template.defaultfilters import last

from .models import Order, orderItem


# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = orderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
