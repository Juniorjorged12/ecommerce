from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at', 'total_price')
    search_fields = ('user__username','user__email')
    readonly_fields = ('created_at', 'updated_at', 'total_price')
    ordering = ('-created_at',)
    inlines = [CartItemInline]

    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = 'Total Price'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'subtotal', 'created_at')
    search_fields = ('cart__user__username', 'product__name')
    readonly_fields = ('subtotal', 'created_at')
    autocomplete_fields = ('product',)

    def subtotal(self, obj):
        return obj.subtotal
    subtotal.short_description = 'Subtotal'
