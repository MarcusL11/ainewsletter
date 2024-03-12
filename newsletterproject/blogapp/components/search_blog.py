import re

from django.core.paginator import Paginator
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django_unicorn.components import UnicornView

from ..models import BlogPost


class SearchBlogView(UnicornView):
    search_content = ""
    show_form = False
    results = []
    page_number = 1
    
    
    def toggle_form(self):
        self.show_form = not self.show_form


    def updated_search_content(self, search_content):
        sanitized_content = escape(search_content.strip())
        sanitized_content = re.sub(r'[^a-zA-Z0-9 ]', '', sanitized_content)
        self.search_content = sanitized_content
        self.page_number = 1
        self.update_results()
        
                
    def updated(self, name, value):
        if name == "search_content":
            self.page_number = 1
            self.update_results()

    
    def highlight_match(self, text, search_term):
        """Highlight the search term in the text, case-insensitively."""
        highlighted_text = re.sub(
            f"({re.escape(search_term)})", 
            r"<mark>\1</mark>", 
            text, 
            flags=re.IGNORECASE
        )
        return mark_safe(highlighted_text)        
    
    
        
    def update_results(self):
        if self.search_content:
            matching_post = BlogPost.objects.filter(title__icontains=self.search_content)

            paginator = Paginator(matching_post, 10)
            page_obj = paginator.get_page(self.page_number)
            
            self.results = page_obj.object_list

            for post in self.results:
                post.title = self.highlight_match(post.title, self.search_content)
            
        else:
            self.results = []
            