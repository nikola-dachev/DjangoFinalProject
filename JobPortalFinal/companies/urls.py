from django.urls import path,include

from JobPortalFinal.companies import views
from JobPortalFinal.companies.views import CompanyListView, CompanyDetailView, CompanyCreateView, CompanyUpdateView, \
    CompanyDeleteView


urlpatterns = [
    path('', CompanyListView.as_view(), name='company list'),
    path('create/', CompanyCreateView.as_view(), name='company create'),
    path('<int:pk>/', include([
        path('', CompanyDetailView.as_view(), name='company details'),
        path('update/', CompanyUpdateView.as_view(), name='company update'),
        path('delete/', CompanyDeleteView.as_view(), name='company delete'),
    ]))
]