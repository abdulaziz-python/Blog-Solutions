
from django.contrib import admin
from .models import Solution, Platform, QuestionType

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'question_type', 'date_added')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('platform', 'question_type')

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
