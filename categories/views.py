from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Category
from . import forms, serializer
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10
    permission_required = 'categories.view_category'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')
    permission_required = 'categories.add_category'


class CategoryDatailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Category
    template_name = 'category_detail.html'
    permission_required = 'categories.view_category'


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    template_name = 'category_update.html'
    success_url = reverse_lazy('category_list')
    form_class = forms.CategoryForm
    permission_required = 'categories.change_category'


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'categories.delete_category'


class CategoryCreateListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializer.CategorySerializer


class CategoryRetriveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializer.CategorySerializer
