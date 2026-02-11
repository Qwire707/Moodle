from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, DateInput, FileInput, CharField, Textarea
from django.urls import reverse_lazy

from accounts.models import CustomUser


class UserRegisterForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'phone', 'avatar', 'bio', 'date_of_birth']
        widgets = {
            'username':TextInput(attrs={'class': 'form-control', 'placeholder': 'Нікнейм'}),
            'email':EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name':TextInput(attrs={'class': 'form-control', 'placeholder': "Ім'я"}),
            'last_name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Прізвище'}),
            'password':PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
            'phone':TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефону'}),
            'avatar':FileInput(attrs={'class': 'form-control'}),
            'bio':TextInput(attrs={'class': 'form-control', 'placeholder': 'Біографія'}),
            'date_of_birth':DateInput(attrs={'class': 'form-control'}),

        }
class LoginForm(AuthenticationForm):
    username = CharField(
        label="Логін",
        widget=TextInput(attrs={"class": "form-control"})
    )
    password = CharField(
        label="Пароль",
        widget=PasswordInput(attrs={"class": "form-control"})
    )

class UserUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "date_of_birth", "avatar", "bio", "phone", 'first_name', 'last_name']
        widgets = {
            "email": EmailInput(attrs={"class": "form-control"}),
            "date_of_birth":DateInput(attrs={"class": "form-control", "type": "date"}),
            "bio": Textarea(attrs={"class": "form-control", "rows": 3}),
            "phone":TextInput(attrs={"class": "form-control"}),
            "first_name": TextInput(attrs={"class": "form-control"}),
            "last_name": TextInput(attrs={"class": "form-control"}),
        }