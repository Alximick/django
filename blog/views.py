from django.shortcuts import render, HttpResponse, render_to_response, redirect
from django.contrib import auth
from blog.models import Article, Comment, Category
from django.template.context_processors import csrf
from blog.forms import CommentForm
from django.core.paginator import Paginator


def hello(request):
    return HttpResponse('Hello World')


def articles(request, page_number=1):
    args = {}
    all_articles = Article.objects.all().order_by('-article_date')
    current_page = Paginator(all_articles, 2)
    args['articles'] = current_page.page(page_number)
    args['username'] = auth.get_user(request).username
    args['projects'] = Category.objects.all()
    return render_to_response('articles.html', args)


def article(request, article_id=1):
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['username'] = auth.get_user(request).username
    args['form'] = CommentForm
    args['comments'] = Comment.objects.filter(comment_article=article_id)
    args['projects'] = Category.objects.all()
    return render_to_response('article.html', args)


def add_comment(request, article_id):
    if request.POST:
        # and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.comment_article = Article.objects.get(id=article_id)
            comments.comment_author = request.user
            form.save()
            # request.session.set_expiry(60)
            # request.session['pause'] = True
    return redirect('/articles/get/{}/'.format(article_id))


def articl_cat(request, category_id=1):
    args = {}
    args['projects'] = Category.objects.all()
    args['category'] = Category.objects.get(id=category_id)
    args['articles'] = Article.objects.filter(category_id=category_id)
    args['username'] = auth.get_user(request).username
    branch_categories = args['category'].get_descendants(include_self=True)
    args['category_articles'] = Article .objects.filter(category__in=branch_categories).distinct()
    return render_to_response('article_cat.html', args)
