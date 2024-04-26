from django.shortcuts import render
from blogapp.models import Blog

# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, 'index.html', context)


def detail(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {"blog": blog}
    return render(request, 'detail.html', context)