from django.shortcuts import render
from .models import BlogPost
from django.http import Http404

def home(request):    
    blogs = BlogPost.objects.all().order_by('-publish_date')
    latest_blog = blogs.first()
    
    context = {
        'blogs': blogs,
        'latest_blog': latest_blog,
    }
    
    return render(request, 'blogapp/index.html', context)

def blog(request, slug):
    try:
        blog = BlogPost.objects.get(slug=slug)
        
        context = {
            'blog': blog,
        }
    
    except BlogPost.DoesNotExist:        
        return Http404("Blog does not exist.")
    
    return render(request, 'blogapp/blog.html', context)




