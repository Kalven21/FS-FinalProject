from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from .models import Post,Categories, Status
from .constants import PUBLISHED_STATUS, SOLD_STATUS
from django.shortcuts import get_object_or_404

class ProductsView(ListView):
    template_name = "products/list.html"
    model = Post
    
    def get_queryset(self):
        queryset = super().get_queryset()
        published = Status.objects.get(id=PUBLISHED_STATUS)
        category = self.kwargs.get('category', None)
        if category:
            category = get_object_or_404(Categories, name=category)
            queryset = queryset.filter(category=category, status=published)
        else:
            queryset = queryset.filter(status=published)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categories.objects.all()
        context["post_list"] = self.get_queryset()
        context['selected_category'] = self.kwargs.get('category', None)
        return context
    
class SoldListView(LoginRequiredMixin, ListView):
    template_name = "products/list.html"
    model = Post
    
    def get_contect_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sold_status = Status.objects.get(id=SOLD_STATUS)
        context["postProducts"] = (
            Post.objects
            .filter(status= sold_status)
            .filter(author= self.request.user)
            .order_by("created_on").reverse()
        )
        return context
    
class ProductDetailView(DetailView):
    template_name = "products/detail.html"
    model = Post

class ProductCreatedView(LoginRequiredMixin, CreateView):
    template_name = "products/new.html"
    model = Post
    fields = ["title", "price", "body", "status", "category" ,"image"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "products/edit.html"
    model = Post
    fields = ["title", "price", "body", "status", "category" , "image"]
    
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "products/delete.html"
    model = Post
    success_url = reverse_lazy("list")
    
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user