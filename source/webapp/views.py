from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Ad


class IndexView(ListView):
    model = Ad
    template_name = 'index.html'
    context_object_name = 'ads'