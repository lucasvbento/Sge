from django.views.generic import ListView, CreateView, DetailView
from .models import Outflow
from . import forms, serializer
from django.urls import reverse_lazy
from app.metrics import get_sales_metrics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10
    permission_required = 'outflows.view_outflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_matrics'] = get_sales_metrics()


class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')
    permission_required = 'outflows.add_outflow'


class OutflowDatailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Outflow
    template_name = 'outflow_detail.html'
    permission_required = 'outflows.view_outflow'


class OutflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = Outflow.objects.all()
    serializer_class = serializer.OutflowSerializer


class OutflowRetriveApiView(generics.RetrieveAPIView):
    queryset = Outflow.objects.all()
    serializer_class = serializer.OutflowSerializer
