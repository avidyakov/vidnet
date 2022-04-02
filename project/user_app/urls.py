from django.urls import path

from .views import UserProfile

app_name = 'user_app'

urlpatterns = [
    path('<int:pk>/', UserProfile.as_view(), name='profile')
]
