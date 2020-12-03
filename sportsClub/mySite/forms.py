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

class loginForm(forms.ModelForm):
    username=forms.CharField(label='Username')
    password=forms.CharField(label='Password')

    class Meta:
        model=login
        fields=['username','password']

TIMINGS = [
('10:00', '10:00'), ('10:30','10:30'), ('11:00', '11:00'), ('11:30','11:30'),
('12:00', '12:00'), ('12:30','12:30'), ('13:00', '13:00'), ('13:30','13:30'),
('14:00', '14:00'), ('14:30','14:30'), ('15:00', '15:00'), ('15:30','15:30'),
('16:00', '16:00'), ('16:30','16:30'), ('17:00', '17:00'), ('17:30','17:30'),
('18:00', '18:00'), ('18:30','18:30'), ('19:00', '19:00')
]

class tabletennisForm(forms.ModelForm):
    LOCS = [('kids', 'Kids Table'), ('adult', 'Adult Table')]
    tablename = forms.ChoiceField(choices=LOCS, label='Choose the type of table')
    resdate = forms.DateField(label='Reservation Date', widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    restime = forms.ChoiceField(choices=TIMINGS, label="Reservation Timing")

    class Meta:
        model = TTReservation
        exclude = ['customer', 'tableName', 'resTime', 'resDate']

    def __init__(self, user, *args, **kwargs):
         self.user = user
         super(tabletennisForm, self).__init__(*args, **kwargs)

class badmintonForm(forms.ModelForm):
    LOCS = [('out', 'Outdoor'), ('in', 'Indoor')]
    btcourtname = forms.ChoiceField(choices=LOCS, label='Choose the type of court')
    btresdate = forms.DateField(label='Reservation Date', widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    btrestime = forms.ChoiceField(choices=TIMINGS, label="Reservation Timing")

    class Meta:
        model = BTReservation
        exclude = ['customer', 'BTCourtName', 'BTresDate', 'BTresTime']

    def __init__(self, user, *args, **kwargs):
         self.user = user
         super(badmintonForm, self).__init__(*args, **kwargs)

T_TIMINGS = [
('7:00', '7:00'), ('7:30','7:30'), ('8:00', '8:00'), ('8:30','8:30'),
('9:00', '9:00'), ('9:30','9:30'), ('10:00', '10:00'), ('10:30','10:30'),
('11:00', '11:00'), ('11:30','11:30'), ('12:00', '12:00'), ('12:30','12:30'),
('13:00', '13:00'), ('13:30','13:30'), ('14:00', '14:00'), ('14:30','14:30'),
('15:00', '15:00'), ('15:30','15:30'), ('16:00', '16:00'), ('16:30','16:30'),
('17:00', '17:00'), ('17:30','17:30'), ('18:00', '18:00'), ('18:30','18:30'),
('19:00', '19:00')
]

class tennisForm(forms.ModelForm):
    LOCS = [('out', 'Outdoor'), ('in', 'Indoor')]
    tcourtname = forms.ChoiceField(choices=LOCS, label='Choose the type of court')
    tresdate = forms.DateField(label='Reservation Date', widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    trestime = forms.ChoiceField(choices=T_TIMINGS, label="Reservation Timing")

    class Meta:
        model = TReservation
        exclude = ['customer', 'TCourtName', 'TresDate', 'TresTime']

    def __init__(self, user, *args, **kwargs):
         self.user = user
         super(tennisForm, self).__init__(*args, **kwargs)

class squashForm(forms.ModelForm):
    LOCS = [('1', 'Floor 1'), ('2', 'Floor 2')]
    scourtname = forms.ChoiceField(choices=LOCS, label='Choose the floor')
    sresdate = forms.DateField(label='Reservation Date', widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    srestime = forms.ChoiceField(choices=T_TIMINGS, label="Reservation Timing")

    class Meta:
        model = SReservation
        exclude = ['customer', 'SCourtName', 'SresDate', 'SresTime']

    def __init__(self, user, *args, **kwargs):
         self.user = user
         super(squashForm, self).__init__(*args, **kwargs)
