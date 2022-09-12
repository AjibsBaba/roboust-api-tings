from django.contrib import admin
from news.models import Author, Article


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date_joined')
    list_filter = ('date_joined',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'date_published')
    list_filter = ('author', 'date_published')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)