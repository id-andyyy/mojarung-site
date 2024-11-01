from django.contrib import admin

from .models import Member, Role


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'role']
    list_display_links = ['name', 'surname']
    ordering = ['time_create']
    list_filter = ['role__title']
    search_fields = ['name', 'surname']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    ordering = ['title']
    search_fields = ['title']
