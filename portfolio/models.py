from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('FE', 'Frontend'),
        ('BE', 'Backend'),
    ]
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('DJ', 'Django'),
        ('FE', 'Frontend'),
        ('FS', 'Full Stack'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=2, choices=[('DJ', 'Django'), ('FE', 'Frontend'), ('FS', 'Full Stack')])
    github_url = models.URLField()
    demo_url = models.URLField(blank=True, null=True)
    technologies_used = models.CharField(max_length=200, help_text="Comma-separated list of technologies", default='none')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=False)


class Certification(models.Model):
    name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    date_issued = models.DateField()
    credential_id = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.issuing_organization}"