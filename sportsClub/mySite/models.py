from django.db import models

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
    birth_date=models.DateField(verbose_name="YYYY-M-DD")
    email=models.EmailField(max_length=15)
    address=models.CharField(max_length=40)
    phone=models.IntegerField()


"""
class TTTable(models.Model):
    #tblName = models.CharField(max_length=15)
    LOCATION_CHOICES = [('1', 'Floor 1'), ('2', 'Floor 2')]
    tblLocation = models.CharField(max_length=2, choices=LOCATION_CHOICES, default='1')

    TYPE_CHOICES = [('kids', 'Kids Table'), ('adult', 'Adult Table')]
    tblType = models.CharField(max_length=5, choices=TYPE_CHOICES, default='adult')

    isReserved = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.tblType} table {self.id} on floor {self.tblLocation})"

class TTReservation(models.Model):
    customer = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='reservations')
    tableName = models.ForeignKey(TTTable, on_delete=models.CASCADE, related_name='tables')
    resDate = models.DateField(default=timezone.now().date())
    resTime = models.TimeField()

    def __str__(self):
        return f'Table {self.tableName.id}: {self.customer} ({self.resDate}, {self.resTime})'
'''
class BTCourt(models.Model):
    LOCATION_CHOICES = [('out', 'Outdoor'), ('in', 'Indoor')]
    crtLocation = models.CharField(max_length=3, choices=LOCATION_CHOICES)


class BTReservation(models.Model):
    BTcustomer = models.ForeignKey(Member, on_delete=models.CASCADE)
    BTcourtName = models.ForeignKey(BTCourt, on_delete=models.CASCADE)
    BTresDate = models.DateField(default=timezone.now().date())
    BTresTime = models.TimeField()

    def __str__(self):
        return f'Table {self.tableName.id}: {self.customer} ({self.resDate}, {self.resTime})'
<<<<<<< HEAD
'''
=======
"""
>>>>>>> ad5a543bda186e0e4e51936c7e400db4b29b3e43
