from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class ChangePasswordView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'main/password_change.html')

    def post(self, request):
        password = request.POST.get('password')
        confirmPassword = request.POST.get('password2')
        u = User.objects.get(username=request.user)

        if password and confirmPassword and password == confirmPassword:
            u.set_password(password)
            update_session_auth_hash(request, u)  # doesnt log out after change
            u.save()
            text = 'Password changed'
            return render(request, 'main/password_change.html', {"text": text})
        text = 'Incorrect password'
        return render(request, 'main/password_change.html', {"text": text})
