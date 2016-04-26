from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView

from bolt_website.forms import *


class IndexView(TemplateView):
    context_object_name = 'index'
    template_name = 'bolt_website/index.html'


class UserLoginView(FormView):
    success_url = reverse_lazy('bolt_usersite:index')
    form_class = UserAuthenticationForm
    template_name = 'bolt_website/login.html'

    def form_valid(self, form):
        user = form.user_cache
        login(request=self.request, user=user)
        return super(UserLoginView, self).form_valid(form)


class UserLogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('bolt_website:index')


class CreateUserView(FormView):
    success_url = reverse_lazy('')
    form_class = RegistrationForm
    template_name = 'bolt_website/registration.html'

    def form_valid(self, form):
        return redirect('bolt_website:index')
