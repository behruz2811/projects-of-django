from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog


# Create your views here.
# def BlogListView(request):
#     blogs = Blog.objects.all()
#
#     context = {
#         'blogs': blogs,
#     }
#
#     return render(request, 'home.html', context=context)
#
#
# def BlogDetailView(request, id):
#     # try:
#     #     blog = Blog.objects.get(id=id)
#     #     context = {
#     #         "blog": blog
#     #     }
#     # except Blog.DoesNotExist:
#     #     raise Http404("Blog topilmadi")
#
#     blog = get_object_or_404(Blog, id=id)
#     context = {
#         "blog":blog
#     }
#
#     return render(request, 'blogdetail.html', context=context)

# Class
class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogdetail.html"
