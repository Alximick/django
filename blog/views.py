from django.shortcuts import render, HttpResponse, render_to_response, redirect
from django.contrib import auth
from blog.models import Article
from django.template.context_processors import csrf
from blog.forms import CommentForm
from django.core.paginator import Paginator

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def articles(request, page_number=1):
    args = {}
    all_articles = Article.objects.all().order_by('-article_date')
    current_page = Paginator(all_articles, 2)
    args['articles'] = current_page.page(page_number)
    args['username'] = auth.get_user(request).username
    return render_to_response('articles.html', args)


def article(request, article_id=1):
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)

def add_comment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            comment.comments_autor = request.user
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/{}/'.format(article_id))

