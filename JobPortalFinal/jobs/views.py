
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from JobPortalFinal.jobs.forms import CreateJobForm, UpdateJobForm
from JobPortalFinal.jobs.models import Job


# Create your views here.
class JobListView(ListView):
    model =Job
    template_name= 'jobs/job-list.html'
    paginate_by = 10

class JobCreateView(CreateView):
    model = Job
    template_name= 'jobs/create-job.html'
    form_class = CreateJobForm
    success_url = reverse_lazy('all jobs')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job-details.html'


class JobUpdateView(UpdateView):
    model = Job
    template_name = 'jobs/update-job.html'
    form_class = UpdateJobForm
    success_url = reverse_lazy('all jobs')



class JobDeleteView(DeleteView):
    model = Job
    template_name = 'jobs/delete-job.html'
    success_url = reverse_lazy('all jobs')


class JobByCategoryView(ListView):
    model = Job
    template_name = 'jobs/job-list.html'

    def get_queryset(self):
        category = self.kwargs.get('category')
        return Job.objects.filter(category=category)


class JobBySearchedNameView(ListView):
    model = Job
    template_name = 'jobs/job-list.html'

    def get_queryset(self):
        query =self.request.GET.get('searched_name')

        if query:
            return Job.objects.filter(title__icontains=query)
