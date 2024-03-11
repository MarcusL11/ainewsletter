from django.core.paginator import Paginator
from django_unicorn.components import UnicornView

from ..models import BlogPost


class PaginationView(UnicornView):
    page_number = 1
    blogs = []
    has_next = False
    has_previous = False
    total_pages = 0
    
    def mount(self):
        self.update_blogs()
        
    def update_blogs(self):
        all_blogs = BlogPost.objects.all().order_by("-publish_date")
        paginator = Paginator(all_blogs, 10)  # 1 item per page as intended
        
        page_obj = paginator.get_page(self.page_number)
        self.blogs = page_obj.object_list  # Ensure this line accurately assigns the paginated set
        
        print(f"Updating blogs for page {self.page_number}: {self.blogs}")  # Debugging

        self.has_next = page_obj.has_next()
        self.has_previous = page_obj.has_previous()
        self.total_pages = paginator.num_pages
        
    def pagination(self, direction):
        if direction == "next" and self.has_next:
            self.page_number += 1
        elif direction == "previous" and self.has_previous:
            self.page_number -= 1
        
        self.update_blogs()
        
