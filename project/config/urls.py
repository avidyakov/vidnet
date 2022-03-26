from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('user_app.urls')),
    path('auth/', include('auth_app.urls')),
    path('friends/', include('friends_app.urls')),

    path('admin/', admin.site.urls),
]
