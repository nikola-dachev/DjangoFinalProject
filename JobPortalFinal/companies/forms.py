from django import forms

from JobPortalFinal.companies.models import Company

class BaseCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['created_by']
        labels = {
            'name': '',
            'description': '',
            'website' : '',
            'logo' : '',
            'location' : '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Company Name: ...'
        self.fields['description'].widget.attrs['placeholder'] = 'Company Description: ...'
        self.fields['website'].widget.attrs['placeholder'] = 'Website URL: ...'
        self.fields['logo'].widget.attrs['placeholder'] = 'Upload your logo...'
        self.fields['location'].widget.attrs['placeholder'] = 'Headquarters: ...'




class CreateCompanyForm(BaseCompanyForm):
    pass


class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['created_by', 'logo']
        labels = {
            'name': '',
            'description': '',
            'website': '',
            'logo': '',
            'location': '',
        }


