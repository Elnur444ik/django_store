from django import forms
from authentication.models import CustomUser


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        try:
            self.user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise forms.ValidationError(f'Пользователя с логином {email} не существует')

        if not self.user.check_password(password):
            raise forms.ValidationError(f'Пароль для логина {email} введён не корректно')


class RegisterForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name', 'email')
