from django import forms

from JobPortalFinal.companies.models import Company
from JobPortalFinal.jobs.models import Job


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['posted_by', 'posted_date']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['location'].widget.attrs['placeholder'] = 'Location'
        self.fields['salary'].widget.attrs['placeholder'] = 'Salary'

        if user:
            self.fields['company'].queryset = Company.objects.filter(created_by=user)

        self.fields['company'].empty_label = "Select your company"
        category_choices = [('', 'Select your job category')] + list(self.fields['category'].choices)
        self.fields['category'].choices = category_choices




class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['posted_by', 'posted_date', 'company']
