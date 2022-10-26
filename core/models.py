from email.policy import default
from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='temp-images',blank=True)
    summary = models.TextField()
    def __str__(self) -> str:
        return self.name 

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Advocate(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,default='')
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="advocates")
    profile_pic = models.ImageField(upload_to='profile_images',blank=True)
    short_bio = models.TextField()
    long_bio = models.TextField()
    advocate_since = models.DateField()


class Link(models.Model):
    advocate  = models.ForeignKey(Advocate,related_name='links',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
    
    def __str__(self) -> str:
        return self.name