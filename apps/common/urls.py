from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('district/<int:pk>', views.DistrictDetailView.as_view(), name='district-detail'),
    path('district/<int:district_pk>/mahalla/<int:pk>', views.MahallaDetailView.as_view(), name='mahalla-detail'),
]