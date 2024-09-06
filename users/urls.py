from django.urls import path
from .views import UserLoginView, user_logout_view, UserRegisterView, UserPasswordChangeView,  UserPasswordResetView, UserPasswordResetDoneView, UserPasswordResetConfirmView, UserProfileView, UserProfileEditView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"), #Class-Based view
    path("register/", UserRegisterView.as_view(), name="register"),
    path("logout/", user_logout_view, name='logout'), #Function-based view
    path("change_password/", UserPasswordChangeView.as_view(), name='change_password'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('profile/<int:user_id>/', UserProfileView.as_view(), name='profile'),
    path("profile_edit/", UserProfileEditView.as_view(), name='profile_edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)