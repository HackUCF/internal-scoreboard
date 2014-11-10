from django.contrib import admin
from django import forms
from competitions.models import Competition, Challenge, ChallengeCategory, Hint


class HintAdminForm(forms.ModelForm):
    fields = ('text',)

    class Meta:
        model = Hint
        widgets = {
            'text': forms.Textarea(attrs={'cols': 120, 'placeholder': 'Put Markdown here!'})
        }


class ChallengeAdminForm(forms.ModelForm):
    class Meta:
        model = Challenge
        widgets = {
            'description': forms.Textarea()
        }


class HintInline(admin.TabularInline):
    model = Hint
    form = HintAdminForm
    extra = 1


class CompetitionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'category', 'competition')
    list_filter = ('category', 'competition')
    search_fields = ('name',)
    inlines = (HintInline, )

    form = ChallengeAdminForm


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(ChallengeCategory)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Hint)