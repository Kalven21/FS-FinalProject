from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        null= True,
        blank = True 
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
