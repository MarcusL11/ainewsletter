from django.contrib import admin
from .models import BlogPost, Tag, TableOfContent


admin.site.register(BlogPost)
admin.site.register(Tag)
admin.site.register(TableOfContent)

