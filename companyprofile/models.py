from django.db import models
from account.models import User
# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=30)
    email = models.EmailField(unique=True, blank=True, null=True)
    profile = models.ImageField(upload_to='company/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name


class Jobs(models.Model):
    job_title = models.CharField(max_length=100)
    skills = models.CharField("Skill(, seprated)", max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title
