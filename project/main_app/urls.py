from django.urls import path

from .views import IndexView

app_name = 'main_app'

urlpatterns = [
    path('', IndexView.as_view()),
]
