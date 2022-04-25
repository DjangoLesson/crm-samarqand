from django.urls import path, include


urlpatterns = [
    path('', include('apps.common.urls')),
    path('', include('apps.core.urls')),
]