from django.conf.urls import url
import blog.views

urlpatterns = [
    url(r'^$', blog.views.articles),
    url(r'^articles/get/(?P<article_id>\d+)/$', blog.views.article)
]
