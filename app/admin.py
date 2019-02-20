from django.contrib import admin
from .models import Category, Question, Team, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('text', 'is_public', 'category')
# Register your models here.

admin.site.register(Category)
admin.site.register(Team)
admin.site.register(Question, QuestionAdmin)
