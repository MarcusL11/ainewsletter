from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import BlogPost


def home(request):
    blogs = BlogPost.objects.all().order_by("-publish_date")
    latest_blog = blogs.first()
    
    page_number = request.GET.get("page")
    first_paginator = Paginator(blogs, 3)
    second_paginator = Paginator(blogs, 10)
    first_page_obj = first_paginator.get_page(page_number)
    second_page_obj = second_paginator.get_page(page_number)
    
    if "HX-Request" in request.headers:
        return render(request, "partials/_index_blog_list.html", {
            "blogs": blogs,
            'first_page_obj': first_page_obj,
            'second_page_obj': second_page_obj,
            "latest_blog": latest_blog,
        })
    
    else:
        
        return render(request, "blogapp/index.html", {
            "blogs": blogs,
            'first_page_obj': first_page_obj,
            'second_page_obj': second_page_obj,
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


def search_trigger(request):
    return render(request, "partials/_search_form.html")


def search_trigger_close(request):
    return render(request, "partials/_search_button.html")


def check_post(request):
    seach_content = request.POST.get("seach-content", "").strip()
    if seach_content:
        matching_title = BlogPost.objects.filter(title__icontains=seach_content)
        matching_tags = BlogPost.objects.filter(tags__name__icontains=seach_content)
        matching_content = BlogPost.objects.filter(content__icontains=seach_content)

        page_number = request.GET.get("page")
        title_paginator = Paginator(matching_title, 3)
        title_page_obj = title_paginator.get_page(page_number)
        
        tags_paginator = Paginator(matching_tags, 3)
        tags_page_obj = tags_paginator.get_page(page_number)
        
        content_paginator = Paginator(matching_content, 3)
        content_page_obj = content_paginator.get_page(page_number)

        context = {
            "matching_title": matching_title,  
            "matching_tags": matching_tags,
            "matching_content": matching_content,
            
            "title_page_obj": title_page_obj,
            "tags_page_obj": tags_page_obj,
            "content_page_obj": content_page_obj,            
        }            
        
        return render(request, "partials/_search_results.html", context)
        
    else: 
        return HttpResponse("")

