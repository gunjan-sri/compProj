from django.db import models

# Create your models here.

# One model for each table
# Migrate after making each model - python3 manage.py makemigrations
# TO apply the changes to the database - python3 manage.py migrate
# Query: table.first(), all()

class Members(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    #DOB = models.DateField()
    email = models.CharField(max_length=50)
    #address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName} (id:{self.id3})"

class ttRegister(models.Model):
    memID = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='registrant')
                # Means that if you delete a memID, it deletes all registered slots.
    tableNo = models.IntegerField()
    regDate = models.DateField()
    regTime = models.TimeField()

    def __str__(self):
        return f"Table Number: {self.tableNo} by {self.memID} for {self.regDate} at {self.regTime}"
