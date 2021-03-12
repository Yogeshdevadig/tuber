from django.db import models

# Create your models here.

class Slider(models.Model):
    headline=models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%y/')
    created_date = models.DateField(auto_now_add=True)
    url = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.headline


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role= models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d")
    created_date = models.DateTimeField(auto_now_add=True)
    y_link = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.first_name

class ContactUsForm(models.Model):
    fullname=models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    company_name=models.CharField(max_length=100)
    subject = models.CharField(max_length=150)
    details = models.TextField()

    def __str__(self):
        return self.email


class Socialmedia(models.Model):
    phone = models.IntegerField()
    email = models.EmailField()
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    youtube= models.CharField(max_length=100)

    def __str__(self):
        return self.email

