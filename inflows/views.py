from django.views.generic import ListView, CreateView, DetailView
from .models import Inflow
from . import forms, serializer
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset


class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.add_inflow'


class InflowDatailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'
    permission_required = 'inflows.view_inflow'


class InflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = serializer.InflowSerializer


class InflowRetriveApiView(generics.RetrieveAPIView):
    queryset = Inflow.objects.all()
    serializer_class = serializer.InflowSerializer
