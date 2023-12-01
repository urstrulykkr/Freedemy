from django.contrib import admin
from django.urls import path, include

# Integrated URLs from all apps.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('allauth.urls')),
]
