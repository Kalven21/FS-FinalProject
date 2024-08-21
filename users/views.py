from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout, update_session_auth_hash
from django.urls import reverse, reverse_lazy
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

class UserPasswordChangeView(PasswordChangeView):
    template_name = "users/password_change_form.html"
    success_url = reverse_lazy('list')
    
    def form_valid(self, form):
        # Update the user's session hash so they don't get logged out after changing the password
        response = super().form_valid(form)
        update_session_auth_hash(self.request, form.user)
        return response
    
class UserPasswordResetView(PasswordResetView):
    template_name = "users/password_reset_form.html"
    email_template_name = "users/password_reset_email.html"
    subject_template_name = 'users/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/password_reset_done.html"

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password_reset_confirm.html"
    success_url = reverse_lazy('list')

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password_reset_complete.html"