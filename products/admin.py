from django.contrib import admin
from .models import Category, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of extra forms to display
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock', 'active', 'created_at', 'updated_at')
    list_filter = ('category', 'active')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock', 'active')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]  # You can add ProductImageInline here if you want to manage images directly in the Product admin

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_primary', 'created_at')
    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return ""
    preview.short_description = 'Imagem'
