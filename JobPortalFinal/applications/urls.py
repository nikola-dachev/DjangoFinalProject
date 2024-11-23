from django.urls import path
from JobPortalFinal.applications import views
from JobPortalFinal.applications.views import JobApplicationCreateView, JobSeekerApplicationListView, \
    ApplicationDetailView, WithdrawApplicationView, EmployerApplicationListView, UpdateApplicationView

urlpatterns = [
    # Private pages (for Job Seekers)
    path('<int:pk>/',JobApplicationCreateView.as_view(), name ='apply'),
    path('my-applications/', JobSeekerApplicationListView.as_view(), name='my applications'),
    path('view/<int:pk>/', ApplicationDetailView.as_view(), name='view application'),
    path('delete/<int:pk>/', WithdrawApplicationView.as_view(), name='withdraw application'),

    # Private pages (for Employers)
    path('employer/view-applications/', EmployerApplicationListView.as_view(), name='employer view applications'),
    path('<int:pk>/update-status/', UpdateApplicationView.as_view(), name='update application'),

]
