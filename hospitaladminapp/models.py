
from django.db import models
from datetime import date
from django.utils.timezone import now
# Create your models here.
class stafflogin(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Inpatient(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=30,blank=True)
    age=models.IntegerField(default=0)
    number=models.BigIntegerField(unique=True)
    gender=models.CharField(max_length=11)
    roomno=models.IntegerField(unique=True,blank=False)
    doctorname=models.CharField(max_length=20)
    medicalcard=models.BooleanField()
    date=models.DateField(default=date.today())
    discharged=models.BooleanField(default=False)

    def __str__(self):
        return(self.name+'  '+self.doctorname)
    
class Outpatient(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=30,blank=True)
    age=models.IntegerField(default=0)
    number=models.BigIntegerField(unique=True)
    gender=models.CharField(max_length=6)
    doctorname=models.CharField(max_length=20)
    date=models.DateField(default=date.today())
    token=models.IntegerField(default=100)
    presc=models.BooleanField(default=False)
   
    def __str__(self):
        return (self.name+'  '+self.doctorname)

        
class doctor(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=30,blank=True,unique=True)
    number=models.BigIntegerField(unique=True)
    department=models.CharField(max_length=20)
    gender=models.CharField(max_length=6)
    offday=models.DateField(default=date.today)
    password=models.CharField(max_length=20,default="pwd")
    def __str__(self):
        return (self.name+'  '+self.department) 

class nurse(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email=models.CharField(unique=True,max_length=30,blank=True)
    number=models.BigIntegerField(unique=True)
    department=models.CharField(max_length=20)
    gender=models.CharField(max_length=6)
    offday=models.DateField(default=date.today())
    def __str__(self):
        return( self.name+'  '+self.department)
class covid(models.Model):
    covax=models.IntegerField()
    coshield=models.IntegerField()
    bed=models.IntegerField()
    def __str__(self):
        return (self.covax+' '+self.coshield+' '+self.bed)

class medicalrecord(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=30)
    records=models.CharField(max_length=200,blank=False)
    medname=models.CharField(max_length=100)
    pres=models.TextField(max_length=500,blank=False)
    qty=models.IntegerField(default=0)
    dt=models.DateField(default=date.today())
    def __str__(self):
        return self.name  

class pharmacy(models.Model):
    token=models.IntegerField()
    name=models.CharField(max_length=30)
    medname=models.CharField(max_length=100,default="null")
    pres=models.TextField(max_length=500)
    contact=models.BigIntegerField(default=0)
    qty=models.IntegerField(default=0)
    dt=models.DateField(default=date.today())
    paid=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class medicine(models.Model):
    medname=models.CharField(max_length=50)
    type=models.CharField(max_length=10)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    def __str__(self):
        return (self.medname+'  '+self.type)

class discharge(models.Model):
    patid=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)
    roomrent=models.IntegerField()
    pharmbill=models.DecimalField(max_digits=7,decimal_places=2)
    paid=models.BooleanField(default=False)

