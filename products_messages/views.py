from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from .models import SendMessage
from django.views import View
from django.shortcuts import render
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
    template_name = "products_messages/mainChats"
    model = SendMessage
    




"""
send > view que guardar el menssage y redirecciona a la pagina de chat

la pagina de chat tiene el id del producto arriba
con el id del product, cargar el product
de el obtienes el seller

y cargas los messages donde el buyer = request.user
and seller = product.author

mandas lo mensages como contexto al template
el template despliega los mensages
"""
