from django.views.generic import DetailView

from .models import User


class UserProfile(DetailView):
    model = User
