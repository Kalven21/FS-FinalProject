from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from .models import SendMessage
from django.views import View
from django.shortcuts import render
from django.db.models import Q
from products.models import Post
from .models import SendMessage
from django.shortcuts  import redirect

class ProductChatView(View, LoginRequiredMixin):
    template_name = "products_messages/chat.html"
    
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        print(product_id)
        product = Post.objects.get(id=product_id)
        messages = SendMessage.objects.filter(
            sender = request.user,
            receiver = product.author,
            product = product
        )
        
        return render(request, self.template_name, {"messages": messages, 'product': product})
    
    def post(self, request, product_id):
        # save the message
        product = Post.objects.get(id=product_id)
        
        sender_id = request.POST.get('sender')     
        receiver_id = request.POST.get('receiver')
        message_text = request.POST.get('message')
        
        SendMessage.objects.create(
            message = message_text,
            sender_id = sender_id,
            receiver_id = receiver_id,
            product = product,
            read = False
        )
        
        return redirect('chat', product_id=product_id)
        

class AllChatsView(View, LoginRequiredMixin):
    template_name = "products_messages/mainChats.html"
    model = SendMessage
    
    def get(self, request, *args, **kwargs):
        user = request.user
        conversations = SendMessage.objects.filter(
            Q(sender=user) | Q(receiver=user)
        ).order_by('sended_time')
        
        unique_conversations = []
        
        for msg in conversations:
            pid = msg.product.id
            exist = any(message.product.id == pid for message in unique_conversations)
            if not exist:
                unique_conversations.append(msg)       
        
        return render(request, self.template_name, {'conversations': unique_conversations})
