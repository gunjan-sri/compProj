from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# One model for each table
# Migrate after making each model - python3 manage.py makemigrations
# TO apply the changes to the database - python3 manage.py migrate
# Query: table.first(), all()

from django.db import models

from django.utils import timezone
# Create your models here.


class Member(models.Model):
    firstname=models.CharField (max_length=100)
    lastname = models.CharField(max_length=100)
    username=models.CharField(max_length=25)
    password1=models.CharField(max_length=30)
    password2=models.CharField(max_length=30)
    birth_date=models.DateField(verbose_name="YYYY-MM-DD")
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=40)
    phone=models.IntegerField(null=True)

class login(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=30)

# Table Tennis Models
class TTTable(models.Model):
    LOCATION_CHOICES = [('1', 'Floor 1'), ('2', 'Floor 2')]
    tblLocation = models.CharField(max_length=2, choices=LOCATION_CHOICES, default='1')
    TYPE_CHOICES = [('kids', 'Kids Table'), ('adult', 'Adult Table')]
    tblType = models.CharField(max_length=5, choices=TYPE_CHOICES, default='adult')
    isReserved = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.tblType} table {self.id} on floor {self.tblLocation}"

class TTReservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    tableName = models.ForeignKey(TTTable, on_delete=models.CASCADE, related_name='tables')
    resDate = models.DateField()
    resTime = models.TimeField()

    def __str__(self):
        return f'Table {self.tableName.id}: {self.customer} ({self.resDate}, {self.resTime})'

# Badminton Models

class BTCourt(models.Model):
    LOCATION_CHOICES = [('out', 'Outdoor'), ('in', 'Indoor')]
    BTcourtLocation = models.CharField(max_length=3, choices=LOCATION_CHOICES)
    isReserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Court {self.id}, {self.BTcourtLocation}"

class BTReservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    BTCourtName = models.ForeignKey(BTCourt, on_delete=models.CASCADE)
    BTresDate = models.DateField()
    BTresTime = models.TimeField()

    def __str__(self):
        return f'Court {self.BTCourtName.id}: {self.customer} ({self.BTresDate}, {self.BTresTime})'

# Tennis Models

class TCourt(models.Model):
    LOCATION_CHOICES = [('out', 'Outdoor'), ('in', 'Indoor')]
    TcourtLocation = models.CharField(max_length=3, choices=LOCATION_CHOICES)
    isReserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Court {self.id}, {self.TcourtLocation}"

class TReservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    TCourtName = models.ForeignKey(TCourt, on_delete=models.CASCADE)
    TresDate = models.DateField()
    TresTime = models.TimeField()

    def __str__(self):
        return f'Court {self.TCourtName.id}: {self.customer} ({self.TresDate}, {self.TresTime})'

# Squash Models

class SCourt(models.Model):
    LOCATION_CHOICES = [('1', 'Floor 1'), ('2', 'Floor 2')]
    ScourtLocation = models.CharField(max_length=2, choices=LOCATION_CHOICES, default='1')
    isReserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Court {self.id}, {self.ScourtLocation}"

class SReservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    SCourtName = models.ForeignKey(SCourt, on_delete=models.CASCADE)
    SresDate = models.DateField()
    SresTime = models.TimeField()

    def __str__(self):
        return f'Court {self.SCourtName.id}: {self.customer} ({self.SresDate}, {self.SresTime})'
