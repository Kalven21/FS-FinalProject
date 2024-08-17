from django.urls import path
from products import views
from .views import contact

urlpatterns = [
    path('', views.ProductsView.as_view(), name="list"),
    path("sold/", views.SoldListView.as_view(), name="sold"),
    path("category/<str:category>/", views.ProductsView.as_view(), name="product_by_category"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.ProductUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view(), name="delete"),
    path("new/", views.ProductCreatedView.as_view(), name="new"),
    path("contact/", contact, name="contact"),
]