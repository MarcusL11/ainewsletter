from django.contrib import admin

from .models import Subscription, User

admin.site.register(User)
admin.site.register(Subscription)


