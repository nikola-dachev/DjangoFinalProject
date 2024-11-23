from django.urls import path, include

from JobPortalFinal.home import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('register-choice/', views.register_choice, name = 'register choice'),
    path('about/', views.about, name = 'about'),
    path('terms-of-service/', views.terms_of_service, name = 'terms of service'),
    path('contact-us/', views.contact_us, name = 'contact us'),
    path('thank-you/', views.thank_you, name = 'thank you'),
]