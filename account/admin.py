from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'phone_number', 'full_name', 'is_staff', 'is_active')

    fieldsets = (
        (
            ('اطلاعات عمومی'),
            {'fields': (
                'username', 'avatar', 'full_name', 'description', 'last_login', 'date_joined','password')}),

        (
            ('راه ارتباطی'),
            {'fields': ("email", 'phone_number',)}),

        (('دسترسی ها'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
                         }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("email", 'phone_number', 'password1', 'password2'),
        }),
    )
