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
