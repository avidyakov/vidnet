from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('main_app.urls')),
    path('user/', include('user_app.urls', namespace='user')),
    path('auth/', include('auth_app.urls', namespace='auth')),
    path('friends/', include('friends_app.urls')),

    path('admin/', admin.site.urls),
]
