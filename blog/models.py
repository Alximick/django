from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.


class Article(models.Model):
    class Meta:
        db_table = 'Article'

    article_title = models.CharField(max_length=150)
    article_text = RichTextField(null=True, blank=True)
    article_text_short = RichTextField(null=True, blank=True)
    article_date = models.DateTimeField(auto_now_add=True, blank=True)
    article_author = models.ForeignKey(User)



class Comment(models.Model):
    class Meta:
        db_table = 'Comment'

    comment_article = models.ForeignKey(Article)
    comment_author = models.ForeignKey(User)
    comment_text = models.TextField(verbose_name='')
    comment_date = models.DateTimeField(auto_now_add=True, blank=True)