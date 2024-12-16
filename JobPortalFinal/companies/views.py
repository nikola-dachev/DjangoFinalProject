
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from JobPortalFinal.companies.forms import CreateCompanyForm, UpdateCompanyForm
from JobPortalFinal.companies.models import Company
from JobPortalFinal.users.models import CustomUser



# Create your views here.
class CompanyListView(ListView):
    model = Company
    template_name= 'companies/company-list.html'


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'companies/company-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = self.object.jobs.all()
        return context

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name= 'companies/create-company.html'
    form_class = CreateCompanyForm
    success_url = reverse_lazy('company list')

    def form_valid(self, form):
        form.instance.created_by= self.request.user
        return super().form_valid(form)



class CompanyUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Company
    template_name = 'companies/update-company.html'
    form_class = UpdateCompanyForm
    success_url = reverse_lazy('company list')
    

    def test_func(self):
        company = self.get_object()
        return self.request.user == company.created_by


class CompanyDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Company
    template_name ='companies/delete-company.html'
    success_url = reverse_lazy('company list')

    def test_func(self):
        company = self.get_object()
        return self.request.user == company.created_by or self.request.user.is_admin()
