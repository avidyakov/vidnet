from django.urls import reverse_lazy
from django.views.generic import CreateView

from auth_app.forms import UserRegForm


class RegView(CreateView):
    form_class = UserRegForm
    template_name = 'auth_app/reg.html'
    success_url = reverse_lazy('auth:login')
