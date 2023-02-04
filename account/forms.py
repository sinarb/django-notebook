from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ValidationError


class RegisterForm(forms.ModelForm):
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'id': 'password2', 'placeholder': 'repeat-password'
    }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            })
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_exist = User.objects.filter(username=username).exists()
        if user_exist:
            raise ValidationError('این نام کاربری از قبل موجود است لطفا نام دیگری انتخاب کنید',code="duplicate_username")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exist = User.objects.filter(email=email).exists()
        if email_exist:
            raise ValidationError('این ایمیل از قبل موجود است لطفا نام دیگری انتخاب کنید',code="duplicate_email")
        return email

    def clean(self):
        cd = super().clean()
        password = cd.get('password')
        re_password = cd.get('re_password')
        if password and re_password and password != re_password:
            raise ValidationError('لطفا تکرا پسورد ها را درست وارد کنید', code='passwords_matching')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username or email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            })
        }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            pass
        else:
            raise ValidationError("یوزنیم یا پسورد اشتباه است!", code="invalid_login")
