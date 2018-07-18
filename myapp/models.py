from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime 
# Create your models here.

class Feedback(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    femail=models.EmailField(null=True)
    subject=models.CharField(max_length=20)
    feedback=models.TextField(max_length=100)

    def __str__(self):
        return self.fname

class profile(models.Model):
    user=models.OneToOneField(User)
    #user = models.ForeignKey(User, unique=True)

    def __str__(self):
        return self.user
    

class Contact(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    phone=models.IntegerField(null=True)
    cemail=models.EmailField(null=True)
    message=models.TextField(max_length=100)
    ngo_choices=(('SP','Saras prayas'),
                    ('V','Vikas'),
                    ('PA','PAWS'),
                    ('PF','Posh Foundation'),
                    ('LN','Lakshyam NGO Delhi'),
                    ('CW','Child & Women Care Society'),
                 ('SA','Shivashrya'),('SK','Satkartar'))
    ngo=models.CharField(max_length=2,choices=ngo_choices,null=True)
    def __str__(self):
        return self.fname


class Email(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email
    

class Comment(models.Model):
    text=models.TextField(null=True)
    created_by=models.ForeignKey(User,null=True,blank=False)
    date=models.DateTimeField(auto_now_add=True,null=True)

class Nested_Comment(models.Model):
    text=models.TextField(null=True)
    created_by=models.ForeignKey(User,null=True,blank=False)
    comment=models.ForeignKey(Comment)
    date=models.DateTimeField(auto_now_add=True,null=True) 



class event(models.Model):
    
    event_name=models.CharField(max_length=100,null=True)
    date=models.IntegerField(null=True)
    month=models.CharField(max_length=10,null=True)
    location=models.CharField(max_length=15,null=True)
    description=models.TextField(blank=True)
    pic=models.FileField(upload_to='pic',null=True)
    time=models.DecimalField(max_digits=10,decimal_places=2,null=True)

    def __str__(self):
         
         
         return self.event_name

class donate(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    phone=models.IntegerField(null=True)
    zipcode=models.IntegerField(null=True)
    demail=models.EmailField(null=True)
    message=models.TextField(max_length=100)
    ngo_choices=(('SP','Saras prayas'),
                    ('V','Vikas'),
                    ('PA','PAWS'),
                    ('PF','Posh Foundation'),
                    ('LN','Lakshyam NGO Delhi'),
                    ('CW','Child & Women Care Society'),
                 ('SA','Shivashrya'),('SK','Satkartar'))
    ngo=models.CharField(max_length=2,choices=ngo_choices,null=True)
    def __str__(self):
        return self.fname        
