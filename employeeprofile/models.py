from django.db import models
from account.models import User

# Create your models here.
class EmployeeProfile(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    portfolio=models.URLField(max_length=100,unique=True,null=True,blank=True)
    contact=models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile/',blank=True,null=True)
    about = models.TextField(blank=True,null=True)
    job_title = models.CharField(blank=True,null=True,max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Degree(models.Model):
    degree_name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.degree_name


class Skill(models.Model):
    skill=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.skill

class Experience(models.Model):
    position=models.CharField(max_length=40)
    company=models.CharField(max_length=40)
    start_date=models.CharField(max_length=20)
    end_date=models.CharField(max_length=20,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.company

class Cv(models.Model):
    cv_name=models.CharField(max_length=50)
    cv_file=models.FileField(upload_to='cv/')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class Project(models.Model):
    project_name=models.CharField(max_length=50)
    project_link=models.URLField(blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name
