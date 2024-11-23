from django.urls import path,include


from JobPortalFinal.jobs.views import JobListView, JobCreateView, JobDetailView, JobUpdateView, JobDeleteView, \
    JobByCategoryView, JobBySearchedNameView

urlpatterns = [
    path('', JobListView.as_view(), name='all jobs'),
    path('create/', JobCreateView.as_view(), name='create job'),
    path('<int:pk>/', include([
        path('', JobDetailView.as_view(), name='job details'),
        path('edit/', JobUpdateView.as_view(), name='job edit'),
        path('delete/', JobDeleteView.as_view(), name='job delete'),
    ])),
    path('category/<str:category>/', JobByCategoryView.as_view(), name='jobs by category'),
    path('search/', JobBySearchedNameView.as_view(), name='jobs by search'),
]