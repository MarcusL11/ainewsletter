from django.core.paginator import Paginator
from django.shortcuts import render

from .models import BlogPost


def home(request):
    blogs = BlogPost.objects.all().order_by("-publish_date")
    latest_blog = blogs.first()
    
    page_number = request.GET.get("page")
    first_paginator = Paginator(blogs, 3)
    first_page_obj = first_paginator.get_page(page_number)
            
    return render(request, "blogapp/index.html", {
        'first_page_obj': first_page_obj,
        "latest_blog": latest_blog,
    })
    

def blog(request, slug):
    try:
        blog = BlogPost.objects.get(slug=slug)

        context = {
            "blog": blog,
        }

    except BlogPost.DoesNotExist:
        return Http404("Blog does not exist.")

    return render(request, "blogapp/blog.html", context)