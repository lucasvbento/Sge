from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Supplier
from . import forms, serializer
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10
    permission_required = 'supplers.view_supplier'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Supplier
    template_name = 'supplier_create.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')
    permission_required = 'supplers.add_supplier'


class SupplierDatailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
    permission_required = 'supplers.view_supplier'


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Supplier
    template_name = 'supplier_update.html'
    success_url = reverse_lazy('supplier_list')
    form_class = forms.SupplierForm
    permission_required = 'supplers.change_supplier'


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')
    permission_required = 'supplers.delete_supplier'


class SupplierCreateListAPIView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = serializer.SupplierSerializer


class SupplierRetriveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = serializer.SupplierSerializer
