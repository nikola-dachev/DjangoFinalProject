from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Your Name")
    phone = forms.CharField(max_length=15, required=True, label="Your Phone Number")
    email = forms.EmailField(required=True, label="Your Email Address")
    request = forms.CharField(widget=forms.Textarea, required=True, label="Your Request")
