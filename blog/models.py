from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    class Meta:
        db_table = 'Article'

    article_title = models.CharField(max_length=150)
    article_text = models.TextField()
    article_text_short = models.TextField()
    article_date = models.DateTimeField(auto_now_add=True)
    article_author = models.ForeignKey(User)
