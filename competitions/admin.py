from django.contrib import admin
from competitions.models import Competition, Challenge


class CompetitionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Challenge)