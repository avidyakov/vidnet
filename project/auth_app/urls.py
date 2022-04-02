from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy

from auth_app.views import RegView

app_name = 'auth_app'

urlpatterns = [
    path('reg/', RegView.as_view()),
    path('login/', LoginView.as_view(
        template_name='auth_app/login.html',
        next_page=reverse_lazy('user:profile')
    ), name='login'),
    path('logout/', LogoutView.as_view())
]
