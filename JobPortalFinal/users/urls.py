
from django.urls import path,include

from JobPortalFinal.users import views
from JobPortalFinal.users.views import ProfileView, SeekerRegisterView, EmployerRegisterView, CustomLoginView, \
    CustomLogoutView, EditProfileView, DeleteProfileView

urlpatterns = [
    path('register/seeker/', SeekerRegisterView.as_view(), name='register seeker'),
    path('register/employer/', EmployerRegisterView.as_view(), name = 'register employer'),
    path('profile/<int:pk>/', include([
        path('', ProfileView.as_view(), name = 'profile'),
        path('edit/', EditProfileView.as_view(), name = 'edit profile'),
        path('delete/', DeleteProfileView.as_view(), name = 'delete profile'),
    ])) ,
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('redirect-to-login/', views.redirect_to_profile, name='redirect to profile'),
]