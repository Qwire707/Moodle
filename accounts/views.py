from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import UserRegisterForm, LoginForm, UserUpdateForm

# Create your views here.
class UserRegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")

class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy("profile")


class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "accounts/profile.html"
    context_object_name = 'user'

    def get_object(self, *args, **kwargs):
        return self.request.user

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self, *args, **kwargs):
        return self.request.user

class UserLogoutView(LoginRequiredMixin, LogoutView):
    success_url = reverse_lazy("login")
