from django.contrib import admin
from news.models import NewsTable


@admin.register(NewsTable)
class NewsAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ("id", "title", "creation_date", "author")
    search_fields = ("id", "author__startswith", "title__startswith")
    list_filter = ("creation_date",)
