from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.urls import reverse
from .forms import UserRegisterForm

class UserLoginView(LoginView):
    template_name = "users/login.html"
    
    def get_success_url(self):
        return reverse('list')

class UserRegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    
    def form_valid(self, form):
        user = form.save(commit=False)
        passw = form.cleaned_data["password"]
        user.set_password(passw) # hash/encript the password
        
        user.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('login')
    
def user_logout_view(request):
    logout(request)
    return redirect('login')

