from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from JobPortalFinal.users.forms import SeekerRegisterForm, EmployerRegisterForm, UpdateSeekerForm, UpdateEmployerForm
from JobPortalFinal.users.models import CustomUser


# Create your views here.
class SeekerRegisterView(CreateView):
    model= CustomUser
    template_name = 'users/register-seeker.html'
    form_class = SeekerRegisterForm

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        custom_user = form.save(commit=False)
        custom_user.user_type = 1
        custom_user.save()
        login(self.request, custom_user)
        return super().form_valid(form)  #i can use and return redirect(self.get_success_url())



class EmployerRegisterView(CreateView):
    model = CustomUser
    template_name = 'users/register-employer.html'
    form_class = EmployerRegisterForm

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        custom_user = form.save(commit=False)
        custom_user.user_type = 2
        custom_user.save()
        login(self.request, custom_user)
        return super().form_valid(form) #i can use and return redirect(self.get_success_url())

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/profile.html'

    def get_object(self,queryset=None):
        return self.request.user

class CustomLoginView(LoginView):
    template_name ='users/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'users/logged_out.html'


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'users/edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

    def get_form_class(self):
        if self.request.user.is_seeker:
            return UpdateSeekerForm
        elif self.request.user.is_employer:
            return UpdateEmployerForm
        return UserChangeForm

    def form_valid(self, form):
        form.save()
        return redirect('profile', pk=self.object.pk)

    def form_invalid(self, form):
        return self.render_to_response({'form': form})


class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model= CustomUser
    template_name = 'users/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, pk=self.request.user.pk)

@login_required
def redirect_to_profile(request):
    return redirect('profile', pk=request.user.pk)


class ListAdminCustomUserView(LoginRequiredMixin,ListView):
    model = CustomUser
    template_name = 'users/admin-users-list.html'

    def get_queryset(self):
        if self.request.user.is_admin():
            return CustomUser.objects.all()

        return CustomUser.objects.none()

class DetailAdminCustomUserView(LoginRequiredMixin,DetailView):
    model = CustomUser
    template_name = 'users/admin-users-details.html'

    def get_object(self, queryset=None):
        user_pk = self.kwargs.get('pk')
        if self.request.user.is_admin() and user_pk:
            return get_object_or_404(CustomUser, pk=user_pk)
        else:
            raise PermissionDenied("You do not have permission to view this page or the user is incorrect.")


class DeleteProfileAsAdminView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'users/admin-delete-user.html'
    success_url = reverse_lazy('all users admin')


    def get_object(self, queryset=None):
        user_pk = self.kwargs.get('pk')
        if self.request.user.is_admin() and user_pk:
            return get_object_or_404(CustomUser, pk=user_pk)
        else:
            raise PermissionDenied("You do not have permission to view this page or the user is incorrect.")
