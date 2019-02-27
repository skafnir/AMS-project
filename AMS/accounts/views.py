from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from accounts.forms import ProfileEditForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class Dashboard(LoginRequiredMixin, View):

    def get(self, request):
        user = User.objects.get(username=request.user)
        return render(request, "accounts/profile_details.html", {'user': user})


class ChangePasswordView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'accounts/password_change.html')

    def post(self, request):
        password = request.POST.get('password')
        confirmPassword = request.POST.get('password2')
        u = User.objects.get(username=request.user)

        if password and confirmPassword and password == confirmPassword:
            u.set_password(password)
            update_session_auth_hash(request, u)  # doesnt log out after change
            u.save()
            text = 'Password changed'
            return render(request, 'accounts/password_change.html', {"text": text})
        text = 'Incorrect password'
        return render(request, 'accounts/password_change.html', {"text": text})


class EditProfileView(LoginRequiredMixin, View):

    def get(self, request):
        user = User.objects.get(username=request.user)
        form = ProfileEditForm(instance=user)
        return render(request, 'accounts/profile_edit.html', {'form': form})

    def post(self, request):
        user = User.objects.get(username=request.user)
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid:
            username = request.POST.get("username")
            email = request.POST.get('email')
            u = User.objects.get(username=request.user)
            users = User.objects.all()
            usernames = []
            emails = []
            for i in users:
                emails.append(i.email)
                usernames.append(i.username)

            if username in usernames and username != request.user.username:
                text = 'Username already taken!'
                return render(request, 'accounts/profile_edit.html', {'form': form, 'text': text})

            elif email in emails and email != request.user.email:
                text = 'Email already in use!'
                return render(request, 'accounts/profile_edit.html', {'form': form, 'text': text})

            form.save()
            return redirect('dashboard')
