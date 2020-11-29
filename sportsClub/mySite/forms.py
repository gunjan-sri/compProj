from django import forms
from .models import Member
from .models import login

class signupForm(forms.ModelForm):
    username=forms.CharField(label='Username')
    firstname=forms.CharField(label='First Name')
    lastname = forms.CharField(label='Last Name')
    birth_date=forms.DateField(label=' Date of Birth')
    email=forms.EmailField(label='Email ID')
    phone=forms.IntegerField(label='Phone Number')
    address=forms.CharField(label='Address')
    password1=forms.CharField(label='Password')
    password2=forms.CharField(label='Confirm Password')

    class Meta:
        model=Member
        fields=['firstname', 'lastname', 'username','birth_date', 'address', 'email', 'password1', 'password2']

class loginForm(forms.ModelForm):
    username=forms.CharField( label='Username')
    password=forms.CharField( label='Password')

    class Meta:
        model=login
        fields=['username','password']

