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
from .models import Post, Status
from .constants import PUBLISHED_STATUS, SOLD_STATUS

class ProductsView(ListView):
    template_name = "products/list.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published = Status.objects.get(id=PUBLISHED_STATUS)
        context["postProducts_list"] = (
            Post.objects
            .filter(status=published)
            .order_by("created_on").reverse()
        )
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
    fields = ["title", "price", "subtitle", "body", "status" ,"image"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "products/edit.html"
    model = Post
    fields = ["title", "price", "subtitle", "body", "status", "image"]
    
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