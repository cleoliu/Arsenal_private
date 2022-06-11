import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.'?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)

class LoginForm(forms.Form):
    username = forms.CharField(
        label="User Name",
        widget=forms.TextInput,
        error_messages={'required': '"User Name" field is required.'}
    )
    password = forms.CharField(
        label="Password",
         widget=forms.PasswordInput,
         error_messages={'required': '"Password" field is required.'})

    def clean_username(self):
        """
        驗證 User Name
        """
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(username__exact=username)
        if not filter_result:
            raise forms.ValidationError('This "User Name" does not exist Please register first')

        return username

class RegistrationForm(UserCreationForm):
    account_type = forms.ChoiceField(label='組織/個人', choices=[(1, "組織"),(0, "個人")])
    username = forms.CharField(label="名字/姓名", error_messages={'required': '"Name" field is required.'})
    email = forms.EmailField(label="管理者信箱", error_messages={'required': '"Email" field is required.'})
    password1 = forms.CharField(label="密碼", strip=False, widget=forms.PasswordInput, error_messages={'required': '"Password" field is required.'},)
    password2 = forms.CharField(label="密碼確認",widget=forms.PasswordInput, error_messages={'required': '"Confirm Password" field is required'})
    address = forms.CharField(label='地址', error_messages={'required': '"Address" field is required.'})
    phone = forms.IntegerField(label='電話', widget = forms.NumberInput, error_messages={'required': '"Phone" field is required.'})
    tax_id = forms.IntegerField(label='統一編號', widget = forms.NumberInput, required=False, initial=0)
    num=[(x, x) for x in range(10)]
    tester = forms.ChoiceField(label='Tester', choices=num, error_messages={'required': '"Tester" field is required.'})
    viewer = forms.ChoiceField(label='Viewer', choices=num, error_messages={'required': '"Viewer" field is required.'})

   # user clean methods to define custom validation rules

    def clean_username(self):
        """
        驗證 Name
        """
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError('"Name" must be at least 3 characters log')
        elif len(username) > 20:
            raise forms.ValidationError('"Name" is too long')
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError('"Name" already exists')
        return username

    def clean_email(self):
        """
        驗證 Email
        """
        email = self.cleaned_data.get('email')
        if email_check(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError('"Email" already exists')
        else:
            raise forms.ValidationError("Please enter a valid email")

        return email

    def clean_password1(self):
        """
        驗證密碼長度
        """
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 3:
            raise forms.ValidationError("your password is too short")
        elif len(password1) > 20:
            raise forms.ValidationError("your password is too long")

        return password1


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, required=False)
    last_name = forms.CharField(label='Last Name', max_length=50, required=False)
    org = forms.CharField(label='Organization', max_length=50, required=False)
    telephone = forms.CharField(label='Telephone', max_length=50, required=False)

class PwdChangeForm(forms.Form):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)

    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
