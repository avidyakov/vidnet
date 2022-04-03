from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from .models import User


class UserView(LoginRequiredMixin):
    model = User


class UserProfile(UserView, DetailView):
    pass


class UserUpdate(UserView, UpdateView):
    login_url = reverse_lazy('auth:login')
    fields = ('email', 'first_name', 'last_name', 'age', 'sex', 'city', 'tags')

    def get_object(self, queryset=None):
        return self.request.user


class UserSubscribers(UserView, DetailView):
    template_name = 'user_app/user_friends.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(object_list=self.get_object().subscribers.all(), **kwargs)


class UserSubscriptions(UserView, DetailView):
    template_name = 'user_app/user_friends.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(object_list=self.get_object().subscriptions.all(), **kwargs)
