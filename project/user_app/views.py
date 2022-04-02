from django.views.generic import DetailView, UpdateView

from .models import User


class UserView:
    model = User


class UserProfile(UserView, DetailView):
    pass


class UserUpdate(UserView, UpdateView):
    fields = ('email', 'first_name', 'last_name', 'age', 'sex', 'city', 'tags')
