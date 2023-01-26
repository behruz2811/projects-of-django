from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.

class HomePageView(ListView):
    model = Post  # listview clasimiz qaysi modeldan foydalanadi
    template_name = 'home.html'
