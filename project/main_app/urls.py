from django.urls import path

from .views import RedirectUserProfile, RedirectIndex

app_name = 'main_app'

urlpatterns = [
    path('', RedirectIndex.as_view(), name='index'),
    path('my/', RedirectUserProfile.as_view(), name='my'),
]
