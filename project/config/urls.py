from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main_app.urls', namespace='main')),
    path('user/', include('user_app.urls', namespace='user')),
    path('auth/', include('auth_app.urls', namespace='auth')),

    path('admin/', admin.site.urls),
]
