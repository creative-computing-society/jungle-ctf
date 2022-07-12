from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Question, BoardLadder, BoardSnake

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

class BoardSnakeAdmin(admin.ModelAdmin):
    list_display = ['boardNo', 'snakeHead', 'snakeTail']
    list_filter = ['boardNo']
    list_per_page = 30
admin.site.register(BoardSnake, BoardSnakeAdmin)

class BoardLadderAdmin(admin.ModelAdmin):
    list_display = ['boardNo', 'ladderBottom', 'ladderTop']
    list_filter = ['boardNo']
    list_per_page = 30
admin.site.register(BoardLadder, BoardLadderAdmin)