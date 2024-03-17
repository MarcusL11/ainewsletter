from django import template
from django.contrib.staticfiles import finders
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def get_image_path(slug, formats=['.webp', '.png']):
    for format in formats:
        image_path = 'image/blog-images/' + slug + format
        if finders.find(image_path):  # Use Django's staticfiles finders
            return static(image_path)
    # Return a default image or an indication that no image was found
    return static('image/blog-images/default.webp')
