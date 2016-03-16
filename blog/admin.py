from django.contrib import admin

# Register your models here.
from blog.models import Article

class Article_Admin(admin.ModelAdmin):
    fields = ['article_title', 'article_text_short', 'article_text','article_author']
    list_display= ['article_title']
    # inlines = [ArticleInLike]
    # list_filter = ['article_date','article_title']
    # search_fields = ['article_title']


admin.site.register(Article, Article_Admin)