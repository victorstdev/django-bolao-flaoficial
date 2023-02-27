from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
# Create your views here.

class IndexView(TemplateView):
    template_name = "bolao/index.html"
