from django.urls import path

from .views import UserProfile, UserUpdate

app_name = 'user_app'

urlpatterns = [
    path('<int:pk>/', UserProfile.as_view(), name='profile'),
    path('<int:pk>/update/', UserUpdate.as_view(), name='update')
]
