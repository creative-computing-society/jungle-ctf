from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Question, Booster, Opposer

# Register your models here.

class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question

class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource
    list_display = ['id', 'body', 'level', 'ans', 'hint']
    list_filter = ['level',]
    list_per_page = 40
    search_fields = ['body', 'ans', 'hint']
admin.site.register(Question, QuestionAdmin)

class OpposerAdmin(admin.ModelAdmin):
    list_display = ['boardNo', 'start', 'end']
    list_filter = ['boardNo']
    list_per_page = 30
admin.site.register(Opposer, OpposerAdmin)

class BoosterAdmin(admin.ModelAdmin):
    list_display = ['boardNo', 'start', 'end']
    list_filter = ['boardNo']
    list_per_page = 30
admin.site.register(Booster, BoosterAdmin)
