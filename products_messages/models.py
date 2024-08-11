from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from products.models import Post

class SendMessage(models.Model):
    message = models.TextField()
    sended_time = models.DateField(auto_now_add=True)
    sender = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )    
    receiver = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="received_messages"
    )
    product = models.ForeignKey(Post, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    image = models.ImageField(upload_to='image_message/', blank=True, null=True)
    