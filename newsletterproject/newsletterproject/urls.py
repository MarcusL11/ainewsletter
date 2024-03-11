from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("unicorn/", include("django_unicorn.urls")),
    path('', include('blogapp.urls')),
    path('', include('authapp.urls')),
]
