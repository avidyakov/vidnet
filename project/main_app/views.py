from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import RedirectView


class RedirectIndex(RedirectView):

    def get_redirect_url(self):
        return reverse('auth:login')


class RedirectUserProfile(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self):
        return reverse('user:profile', args=[self.request.user.id])
