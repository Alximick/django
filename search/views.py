from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse
from blog.models import Article, Category


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    args = {}
    if 'q' in request.GET and request.GET['q']:
        args['query'] = request.GET['q']
        args['projects'] = Category.objects.all()
        q = request.GET['q']
        args['articles'] = Article.objects.filter(article_title=q)
        return render_to_response('search_results.html', args)
    else:
        return HttpResponse('Please submit a search term.')
