from django.conf.urls import url
import blog.views

urlpatterns = [
    url(r'^$', blog.views.articles),
    url(r'^articles/get/(?P<article_id>\d+)/$', blog.views.article),
    url(r'^articles/all$', blog.views.article),
    url(r'^page/(\d+)/$', blog.views.articles),
    url(r'^articles/add_comment/(?P<article_id>\d+)/$', blog.views.add_comment),
    url(r'^category/get/(?P<category_id>\d+)/$', blog.views.articl_cat),
]
