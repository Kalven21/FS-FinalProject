from django.urls import path
from products_messages import views

urlpatterns = [
    path('/', views.AllChatsView.as_view(), name="allChats"),
    path("chat/<int:product_id>/", views.ProductChatView.as_view(), name="chat"),
]