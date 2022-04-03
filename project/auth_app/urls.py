from django.urls import path

from auth_app.views import RegView, UserLoginView, UserLogoutView

app_name = 'auth_app'

urlpatterns = [
    path('reg/', RegView.as_view(), name='reg'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout')
]
