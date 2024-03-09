from django.shortcuts import render
from .models import BlogPost
from django.http import Http404
from django.http import HttpResponse


def home(request):
    blogs = BlogPost.objects.all().order_by("-publish_date")
    latest_blog = blogs.first()

    context = {
        "blogs": blogs,
        "latest_blog": latest_blog,
    }

    return render(request, "blogapp/index.html", context)


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
    return render(request, "partials/_search_blog.html")


def search_trigger_close(request):
    return render(request, "partials/_search_button.html")


def check_post(request):
    seach_content = request.POST.get("seach-content", "").strip()
    if seach_content:
        matching_title = BlogPost.objects.filter(title__icontains=seach_content)
        matching_tags = BlogPost.objects.filter(tags__name__icontains=seach_content)
        matching_content = BlogPost.objects.filter(content__icontains=seach_content)

        context = {
            "matching_title": matching_title,  
            "matching_tags": matching_tags,
            "matching_content": matching_content,
        }            
        
        return render(request, "partials/_search_results.html", context)
        
    else: 
        return HttpResponse("")

