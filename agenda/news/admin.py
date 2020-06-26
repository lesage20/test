from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'author','image' ]
    search_field = ['title', 'date']
    list_filter = ('status',)
    ordering = ['date_add','title', 'date']
    fieldsets = [
                ("Info CategorieArticle", {"fields":['name', 'image', 'description']}),
                ("Standard", {"fields":['status']})
                ]
    list_per_page = 10
    date_hierarchy = "date_add"

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['commentator', 'article', 'message']
    search_field = ['message']
    list_filter = ('status',)
    ordering = ['date_add',]
    fieldsets = [
                ("Info CategorieArticle", {"fields":['name', 'image', 'description']}),
                ("Standard", {"fields":['status']})
                ]
    list_per_page = 10
    date_hierarchy = "date_add"


