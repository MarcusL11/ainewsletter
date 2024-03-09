from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/<slug:slug>/", views.blog, name="blog"),
]


htmx_urlpatterns = {
    path("search/", views.search_trigger, name="search-trigger"),    
    path("search/close/", views.search_trigger_close, name="search-trigger-close"),
    path("check_post/", views.check_post, name="check-post"),
}

urlpatterns += htmx_urlpatterns
