from django import forms

from JobPortalFinal.applications.models import Application


class JobApplicationCreateForm(forms.ModelForm):

    clear_resume = forms.BooleanField(required=False, initial=False, label="Clear Resume")

    class Meta:
        model = Application
        fields = ['skills', 'resume']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['skills'].widget.attrs['placeholder'] = "List your skills..."
        self.fields['resume'].help_text = "Please upload your resume"

