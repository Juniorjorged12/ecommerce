from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'cpf', 'birth_date')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )
    search_fields = ('username', 'email','cpf',)
    ordering = ('username',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ('user', 'street', 'number', 'city', 'state', 'zip_code')
    list_filter = ('state', 'city')
    search_fields = ('user__username', 'street', 'city', 'zip_code')
    ordering = ('user', 'city')