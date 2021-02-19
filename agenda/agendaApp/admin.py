from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',  ]
    list_filter = ('status',)
    search_field = ['name',]
    ordering = ['date_add','name']
    fieldsets = [
                ("Info CategorieArticle", {"fields":['name', 'image', 'description']}),
                ("Standard", {"fields":['status']})
                ]
    list_per_page = 10
    date_hierarchy = "date_add"

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['nom',  ]
    search_field = ['nom',]
    ordering = ['date_add','nom']

@admin.register(models.UpcomingEvent)
class UpcomingEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'begin_date', 'end_date', 'speakers' ]
    search_field = ['title',]
    ordering = ['date_add','title']


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'begin_date', 'end_date', 'location', 'category','image' ]
    search_field = ['title', 'category', 'location', 'begin_date']
    list_filter = ('status',)
    ordering = ['date_add','title']
    fieldsets = [
                ("Info CategorieArticle", {"fields":['title', 'image', ]}),
                ("Standard", {"fields":['status']})
                ]
    list_per_page = 10
    date_hierarchy = "date_add"
    
    def image_view(self,obj):
        return mark_safe('<img src="{url}" width=100 height=50>'.format(url=obj.image.url))


