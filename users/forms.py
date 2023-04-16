from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    age = forms.IntegerField(min_value=18, required=False)

class UserForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    credit_card = forms.IntegerField(min_value=16)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
