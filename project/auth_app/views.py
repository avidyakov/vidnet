from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from auth_app.forms import UserRegForm


class RegView(CreateView):
    form_class = UserRegForm
    template_name = 'auth_app/reg.html'
    success_url = reverse_lazy('auth:login')


class UserLoginView(LoginView):
    template_name = 'auth_app/login.html'
    next_page = reverse_lazy('main:my')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('auth:login')
