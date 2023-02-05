from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from authentication.forms import LoginForm


# class LoginUser(LoginView):
#     form_class = LoginForm
#     template_name = 'auth/login.html'


class LoginUser(TemplateView):
    template_name = 'auth/login.html'

    def post(self, request):
        context = {'login_form': LoginForm}
        login_form = LoginForm(request.POST)
        print('hello')
        print(login_form)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('store')
            return render(request, 'auth/login.html', context)
        else:
            context = {
                'login_form': login_form,
            }
            return render(request, 'auth/login.html', context)

    def get(self, request):
        context = {'login_form': LoginForm}
        return render(request, 'auth/login.html', context)


class RegisterView(TemplateView):
    template_name = 'auth/register.html'

    def get(self, request):
        user_form = RegisterForm
        context = {'user_form': user_form}
        return render(request, 'auth/register.html', context)

    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('store')

        context = {'user_from': user_form}
        return render(request, 'auth/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('store')
