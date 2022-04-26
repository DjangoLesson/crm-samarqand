from django.shortcuts import render
from django.views import generic
from . import models


class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = models.District.objects.all()
        return context


class DistrictDetailView(generic.DetailView):
    queryset = models.District.objects.all()
    

class MahallaDetailView(generic.DetailView):
    queryset = models.Mahalla.objects.all()

class StreetDetailView(generic.DetailView):
    queryset = models.Street.objects.all()


class HouseDetailView(generic.DetailView):
    queryset = models.House.objects.all()
