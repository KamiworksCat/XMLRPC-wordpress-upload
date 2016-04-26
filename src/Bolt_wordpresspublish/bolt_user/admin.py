from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class BoltUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Important dates'), {'fields': ('last_login', 'created', 'modified')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Wordpress Information'), {'fields': ('wordpress_link', 'wordpress_id', 'wordpress_pass')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'created', 'modified')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('created', 'modified')
    ordering = ('email',)

admin.site.register(User, BoltUserAdmin)
