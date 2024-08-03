from django.contrib import admin
from .models import Status, Categories, Post

# Register your models here.

admin.site.register(Status)
admin.site.register(Categories)
admin.site.register(Post)