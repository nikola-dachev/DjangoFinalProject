from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from JobPortalFinal.users.models import CustomUser, Profile


class SeekerRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    resume = forms.FileField(required=False)
    skills = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'resume','skills' ]


    def save(self, commit=True):
        custom_user = super().save(commit=False)
        custom_user.is_seeker = True
        if commit:
            custom_user.save()
            Profile.objects.create(custom_user=custom_user, resume=self.cleaned_data.get('resume'),
                                   skills=self.cleaned_data.get('skills'))

        return custom_user



class EmployerRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    company_name= forms.CharField(required=True)
    website= forms.URLField(required=True)
    logo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username','email', 'password1', 'password2', 'company_name', 'website', 'logo']

    def save(self,commit=True):
        custom_user = super().save(commit=False)
        custom_user.is_employer = True

        if commit:
            custom_user.save()
            Profile.objects.create(custom_user = custom_user, company_name= self.cleaned_data.get('company_name'),
                                   website= self.cleaned_data.get('website'),
                                   logo= self.cleaned_data.get('logo')
                                   )

        return custom_user


class UpdateSeekerForm(UserChangeForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    resume = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'placeholder': 'Upload your resume'}))
    skills = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your skills'}), required=False)


    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your old password'}), required=False, label="Old Password")
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your new password'}), required=False, label="New Password")
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your new password'}), required=False, label="Confirm New Password")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'skills']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if new_password and new_password != confirm_new_password:
            self.add_error('confirm_new_password', 'New passwords do not match.')

        return cleaned_data

    def save(self, commit=True):
        custom_user = super().save(commit=False)

        if commit:
            custom_user.save()


            profile = Profile.objects.get(custom_user=custom_user)
            profile.resume = self.cleaned_data.get('resume', profile.resume)
            profile.skills = self.cleaned_data.get('skills', profile.skills)
            profile.save()


            if self.cleaned_data.get('new_password'):
                custom_user.set_password(self.cleaned_data['new_password'])
                custom_user.save()

        return custom_user


class UpdateEmployerForm(UserChangeForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    company_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your company name'}))
    website = forms.URLField(required=True, widget=forms.URLInput(attrs={'placeholder': 'Enter your website URL'}))
    logo = forms.ImageField(required=False)


    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your old password'}), required=False, label="Old Password")
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your new password'}), required=False, label="New Password")
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your new password'}), required=False, label="Confirm New Password")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'website', 'logo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False


    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if new_password and new_password != confirm_new_password:
            self.add_error('confirm_new_password', 'New passwords do not match.')

        return cleaned_data

    def save(self, commit=True):
        custom_user = super().save(commit=False)

        if commit:
            custom_user.save()


            profile = Profile.objects.get(custom_user=custom_user)  # Assuming one profile per user
            profile.company_name = self.cleaned_data.get('company_name', profile.company_name)
            profile.website = self.cleaned_data.get('website', profile.website)
            profile.logo = self.cleaned_data.get('logo', profile.logo)
            profile.save()


            if self.cleaned_data.get('new_password'):
                custom_user.set_password(self.cleaned_data['new_password'])
                custom_user.save()

        return custom_user
