from django.contrib import admin
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('News_title', 'News_description')


admin.site.register(News,NewsAdmin)

# Register your models here.
