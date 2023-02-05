from django import forms
from django.contrib.auth.forms import AuthenticationForm
# from django.core.exceptions import ValidationError

from authentication.models import CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            try:
                self.user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                raise forms.ValidationError(f'Пользователь с эл. почтой {email} не зарегистрирован.')
            if not self.user.check_password(password):
                raise forms.ValidationError(f'Неверный пароль.')
        elif not email:
            raise forms.ValidationError(f'Введите корректный адрес эл. почты.')
        elif not password:
            raise forms.ValidationError(f'Введите пароль.')
        return self.cleaned_data

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password', 'first_name', 'last_name')
