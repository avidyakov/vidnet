from django.urls import path

from .views import UserProfile, UserUpdate, UserSubscribers, UserSubscriptions

app_name = 'user_app'

urlpatterns = [
    path('<int:pk>/', UserProfile.as_view(), name='profile'),
    path('<int:pk>/subscribers/', UserSubscribers.as_view(), name='subscribers'),
    path('<int:pk>/subscriptions/', UserSubscriptions.as_view(), name='subscriptions'),
    path('update/', UserUpdate.as_view(), name='update'),
]
