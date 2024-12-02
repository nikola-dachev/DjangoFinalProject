from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import JobApplicationCreateForm
from .models import Application
from django.contrib import messages


from django.contrib.auth.mixins import LoginRequiredMixin

from ..companies.models import Company
from ..jobs.models import Job


class JobApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    form_class = JobApplicationCreateForm
    template_name = 'applications/apply-for-a-job.html'

    def get_success_url(self):
        return reverse('all jobs')

    # i need to fetch the job so i pass it to the template to send me back to the particular job
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = get_object_or_404(Job, pk=self.kwargs['pk'])
        return context


    def form_valid(self, form):
        if not self.request.user.is_seeker:
            messages.error(self.request, 'Only Job Seekers can apply for this job')
            return redirect('home')

        job = get_object_or_404(Job, pk = self.kwargs['pk'])
        form.instance.applicant = self.request.user
        form.instance.job = job
        form.instance.status = 'Pending'

        profile =self.request.user.profile

        # if clear resume is ticked i will remove the uploaded file
        if form.cleaned_data.get('clear_resume'):
            profile.resume = None
        else:
            profile.resume = form.cleaned_data.get('resume') or profile.resume

        profile.save()

        return super().form_valid(form)


class JobSeekerApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'applications/my-applications.html'

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)


class ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = Application
    template_name = 'applications/application_detail.html'

    def get_object(self, queryset=None):

        application = super().get_object(queryset)
        if application.applicant != self.request.user:
            raise Http404("You are not authorized to view this application.")
        return application


class WithdrawApplicationView(DeleteView):
    model = Application
    template_name = 'applications/withdraw-application.html'


    def get_object(self, queryset=None):
        application = super().get_object(queryset)
        if application.applicant != self.request.user:
            raise Http404("You are not authorized to view this application.")
        return application

    def get_success_url(self):
        messages.success(self.request, "Your application has been withdrawn successfully.")
        return reverse_lazy('my applications')


# Employer's view of applications for a specific job (Private)
class EmployerApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'applications/employer-view-applications.html'


    def get_queryset(self):
        user = self.request.user
        if user.is_employer():
            company = get_object_or_404(Company, created_by = user)
            jobs = Job.objects.filter(company=company)
            return Application.objects.filter(job__in=jobs)

        # i have validation for the type of user in the base template as well
        return Application.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class UpdateApplicationView(LoginRequiredMixin, UpdateView):
    model = Application
    fields= ['status']
    template_name = 'applications/update-application-status.html'

    def get_queryset(self):
        company = get_object_or_404(Company, created_by = self.request.user)
        jobs = Job.objects.filter(company=company)
        return Application.objects.filter(job__in=jobs)

    def form_valid(self, form):
        messages.success(self.request, "Your application has been updated successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employer view applications')