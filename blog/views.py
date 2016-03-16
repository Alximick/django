from django.shortcuts import render, HttpResponse, render_to_response
from django.contrib import auth
from blog.models import Article

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def articles(request):
    args = {}
    args['articles'] = Article.objects.all()
    args['username'] = auth.get_user(request).username
    return render_to_response('articles.html', args)


def article(request, article_id=1):
    args = {}
    # args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)