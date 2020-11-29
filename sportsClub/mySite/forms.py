from django import forms
from .models import *

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

class tabletennisForm(forms.ModelForm):
    LOCS = [('kids', 'Kids Table'), ('adult', 'Adult Table')]
    tablename = forms.ChoiceField(choices=LOCS, label='Choose the type of table')
    TIMINGS = [
    ('10:00', '10:00'), ('10:30','10:30'), ('11:00', '11:00'), ('11:30','11:30'),
    ('12:00', '12:00'), ('12:30','12:30'), ('13:00', '13:00'), ('13:30','13:30'),
    ('14:00', '14:00'), ('14:30','14:30'), ('15:00', '15:00'), ('15:30','15:30'),
    ('16:00', '16:00'), ('16:30','16:30'), ('17:00', '17:00'), ('17:30','17:30'),
    ('18:00', '18:00'), ('18:30','18:30'), ('19:00', '19:00')
    ]
    restime = forms.ChoiceField(choices=TIMINGS, label="Reservation Timing")
    resdate = forms.DateField(label='Reservation Date', widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))

    class Meta:
        model = TTReservation
        exclude = ['customer', 'tableName', 'resTime', 'resDate']

    def __init__(self, user, *args, **kwargs):
         self.user = user
         super(tabletennisForm, self).__init__(*args, **kwargs)

class loginForm(forms.ModelForm):
    username=forms.CharField(max_length=25, label='Username')
    password=forms.CharField(max_length=30, label='Password')
