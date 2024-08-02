from django.urls import path
from .views import UserLoginView, user_logout_view, UserRegisterView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"), #Class-Based view
    path("register/", UserRegisterView.as_view(), name="register"),
    path("logout/", user_logout_view, name='logout'), #Function-based view
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)