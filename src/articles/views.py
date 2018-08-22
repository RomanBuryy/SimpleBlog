from django.shortcuts import render

from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from . models import Article
# Create your views here.

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


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


class ArticleUpdateView(UpdateView):

    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'text']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    context_object_name = 'batman'
    success_url = reverse_lazy('home')
