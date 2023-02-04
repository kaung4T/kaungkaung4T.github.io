from django.db import models
from django.contrib.auth.models import auth, AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class Profile(AbstractUser):
    image = models.ImageField(upload_to='media')


class Work(models.Model):
    user = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=225, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to="work")


class Work_project(models.Model):
    user = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date= models.DateField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    image1 = models.ImageField(upload_to="work_project")
    image2 = models.ImageField(upload_to="work_project")
    image3 = models.ImageField(upload_to="work_project")
    image4 = models.ImageField(upload_to="work_project")


class About(models.Model):
    user = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE)
    about = models.TextField()
    conclusion = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    nation = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    github = models.CharField(max_length=255, null=True, blank=True)
    leet = models.CharField(max_length=255, null=True, blank=True)
    linked = models.CharField(max_length=255, null=True, blank=True)
    graduate = models.CharField(max_length=255, null=True, blank=True)
    nation_url = models.URLField(null=True, blank=True)
    work = models.CharField(max_length=255, null=True, blank=True)
    work_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"

class Skill(models.Model):
    language_proficient = models.CharField(max_length=255)
    language_familiar = models.CharField(max_length=255)
    backend = models.CharField(max_length=255)
    frontend = models.CharField(max_length=255)
    tools = models.CharField(max_length=255)
    first_language = models.CharField(max_length=255)
    second_language = models.CharField(max_length=255)
    api = models.CharField(max_length=255)

class Project(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='project_image')
    uses = models.CharField(max_length=255)
    description = models.TextField()
    schoolp = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    source_code = models.URLField(max_length=255, blank=True, null=True)
    image2 = models.ImageField(upload_to='project_image', null=True, blank=True)
    image3 = models.ImageField(upload_to='project_image', null=True, blank=True)
    image4 = models.ImageField(upload_to='project_image', null=True, blank=True)
    date = models.CharField(null=True, blank=True, max_length=255)

class SchoolProject(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='project_image')
    uses = models.CharField(max_length=255)
    description = models.TextField()



class Education(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    date = models.CharField(max_length=225)
    total_date = models.CharField(max_length=225, null=True, blank=True)
    gpa = models.CharField(max_length=225, null=True, blank=True)
    major = models.CharField(max_length=225, null=True, blank=True)

class Education_tran(models.Model):
    image = models.ImageField(upload_to='education_image')
    title = models.CharField(max_length=225, null=True, blank=True)
    url = models.URLField(null=True, blank=True)