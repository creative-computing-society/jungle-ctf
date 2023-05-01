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
    list_per_page = 80
    search_fields = ['body', 'ans', 'hint']
admin.site.register(Question, QuestionAdmin)

class OpposerResource(resources.ModelResource):
    class Meta:
        model = Opposer

class OpposerAdmin(ImportExportModelAdmin):
    resource_class = OpposerResource
    list_display = ['boardNo', 'start', 'end']
    list_filter = ['boardNo']
    list_per_page = 30
admin.site.register(Opposer, OpposerAdmin)

class BoosterResource(resources.ModelResource):
    class Meta:
        model = Booster

class BoosterAdmin(ImportExportModelAdmin):
    resource_class = BoosterResource
    list_display = ['boardNo', 'start', 'end']
    list_filter = ['boardNo']
    list_per_page = 30
admin.site.register(Booster, BoosterAdmin)
