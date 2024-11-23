from django.shortcuts import render, redirect

from JobPortalFinal.companies.models import Company
from JobPortalFinal.home.forms import ContactForm
from JobPortalFinal.home.models import ContactMessage


# Create your views here.
def index(request):
    companies = Company.objects.all()[:4]
    context = {
        'companies':companies
    }

    return render(request,'home/index.html',context)

def register_choice(request):
    return render(request, 'home/register-choice.html')


def about(request):
    return render(request, 'home/about.html')

def terms_of_service(request):
    return render(request, 'home/terms_of_service.html')

def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_message = ContactMessage(
                name = contact_form.cleaned_data['name'],
                phone=contact_form.cleaned_data.get('phone'),
                email=contact_form.cleaned_data['email'],
                request=contact_form.cleaned_data['request']
            )
            contact_message.save()

            return redirect('thank you')

    else:
        contact_form = ContactForm()

    context = {
        'contact_form':contact_form
    }
    return render(request, 'home/contact-us.html',context)


def thank_you(request):
    return render(request, 'home/thank-you.html')