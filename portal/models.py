from django.db import models

class doctor(models.Model):
    emailId = models.EmailField(primary_key=True, max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    speciality = models.CharField(max_length=30)
    patients = models.CharField(max_length=30)

    def __unicode__(self):
        return self.firstName

class patient(models.Model):
    emailId = models.EmailField(primary_key=True, max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.firstName

class profile(models.Model):
    emailId = models.EmailField(primary_key=True, max_length=30)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    phone = models.IntegerField(max_length=15)
    address = models.TextField(max_length=60)

    def __unicode__(self):
        return self.emailId

class diagnosis(models.Model):
    ailment = models.CharField(max_length=30)
    doctorName = models.CharField(max_length=30)
    doctorEmail = models.CharField(max_length=30)
            
class appointment(models.Model):
    doctorEmail = models.EmailField(max_length=30)
    patientEmail = models.EmailField(max_length=30)
    last = models.DateField(max_length=30)
    next = models.DateField(max_length=30)

class onlineConsultation(models.Model):
    last = models.DateField(max_length=30)
    next = models.DateField(max_length=30)

class allergie(models.Model):
    email = models.EmailField(max_length=30, unique=True)
    allergies = models.TextField(max_length=30)

class messages(models.Model):
    destination = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    def __unicode__(self):
        return self.source