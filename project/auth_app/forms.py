from django.contrib.auth.forms import UserCreationForm

from user_app.models import User


class UserRegForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'age', 'sex', 'tags', 'city')
