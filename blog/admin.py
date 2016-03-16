from django.contrib import admin
from blog.models import Article, Category


class Article_Admin(admin.ModelAdmin):
    fields = ['article_title', 'article_text_short',
              'article_text', 'article_author', 'category']
    list_display = ['article_title']
    list_filter = ['article_date', 'article_title']
    search_fields = ['article_title']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']


admin.site.register(Article, Article_Admin)
admin.site.register(Category, CategoryAdmin)
