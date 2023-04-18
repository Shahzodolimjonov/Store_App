from django.contrib import admin

from configapp.models import News,Category


# Register your models here.


class NewsAdmins(admin.ModelAdmin):
    list_display = ('id', 'title','content', 'created_at', 'is_published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)


admin.site.register(News, NewsAdmins)
admin.site.register(Category)