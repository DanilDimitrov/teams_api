from django.contrib import admin
from .models import Team, Person


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'team')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('team',)
    list_select_related = ('team',)


admin.site.register(Team, TeamAdmin)
admin.site.register(Person, PersonAdmin)
