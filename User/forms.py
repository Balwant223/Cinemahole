from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
class SignUpForm(forms.ModelForm):
    password=forms.CharField(label='Password',
                             widget=forms.PasswordInput)
    re_password=forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','first_name','email')
    def clean_data(self):
        cd=self.cleaned_data
        if cd['password']!=cd['re_password']:
            raise forms.ValidationError('Password didn\'t match.')
        return cd['re_password']