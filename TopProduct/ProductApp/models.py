from django.db import models

class USerData(models.Model):
    companyName = models.CharField(max_length=20)
    clientID = models.CharField(max_length=100)
    clientSecret = models.CharField(max_length=100)
    ownerName = models.CharField(max_length=50)
    ownerEmail =  models.EmailField()
    rollNo = models.IntegerField()

    def __str__(self):
        return self.companyName

class Companies(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

