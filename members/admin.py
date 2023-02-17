from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member

class MemberAdmin(UserAdmin):
    list_display = ('email', 'name', 'gender', 'age', 'activity_level', 'is_staff')
    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'gender', 'age', 'activity_level')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'gender', 'age', 'activity_level', 'password1', 'password2'),
        }),
    )

admin.site.register(Member, MemberAdmin)
