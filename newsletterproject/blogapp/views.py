from django.shortcuts import render
from .models import BlogPost


def home(request):    
    blogs = BlogPost.objects.all()
    latest_blog = blogs.first()
    
    context = {
        'blogs': blogs,
        'latest_blog': latest_blog,
    }
    
    return render(request, 'blogapp/index.html', context)

def blog(request):
    
    return render(request, 'blogapp/blog.html')