from django.shortcuts import render

from django.views.generic import ListView, DetailView
from . models import Article
# Create your views here.

from django.views.generic.edit import CreateView



class ArticlesListView(ListView):
    model = Article
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'batman'



class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = '__all__'
