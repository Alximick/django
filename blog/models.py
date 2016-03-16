from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import mptt
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    class Meta():
        db_table = 'category'
        verbose_name_plural = "Категории"
        verbose_name = "Категория"
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=150)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children',
                            verbose_name='parent class')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_py = ['name']


mptt.register(Category, order_insertion_by=['name'])


class Article(models.Model):
    class Meta:
        db_table = 'Article'
        verbose_name_plural = "Статьи"

    article_title = models.CharField(max_length=150)
    article_text = RichTextField(null=True, blank=True)
    article_text_short = RichTextField(null=True, blank=True)
    article_date = models.DateTimeField(auto_now_add=True, blank=True)
    article_author = models.ForeignKey(User)
    category = TreeForeignKey(Category,  blank=True, null=True)


class Comment(models.Model):
    class Meta:
        db_table = 'Comment'

    comment_article = models.ForeignKey(Article)
    comment_author = models.ForeignKey(User)
    comment_text = models.TextField(verbose_name='')
    comment_date = models.DateTimeField(auto_now_add=True, blank=True)
