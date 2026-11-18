from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','status', 'created_at', 'updated_at', 'total_price')
    list_editable = ('status',)
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at', 'total_price')
    ordering = ('-created_at',)
    inlines = [OrderItemInline]

    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = 'Total Price'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price', 'subtotal', )
    search_fields = ('order__user__username', 'product__name',)
    readonly_fields = ('created_at',)
