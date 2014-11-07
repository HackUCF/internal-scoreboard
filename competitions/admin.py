from django.contrib import admin
from competitions.models import Competition, Challenge, ChallengeCategory


class CompetitionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'category', 'competition')
    list_filter = ('category', 'competition')
    search_fields = ('name',)

admin.site.register(Competition, CompetitionAdmin)
admin.site.register(ChallengeCategory)
admin.site.register(Challenge, ChallengeAdmin)