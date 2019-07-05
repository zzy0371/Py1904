from django.contrib import admin
from .models import Question,Choice,Temp
# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Temp)
