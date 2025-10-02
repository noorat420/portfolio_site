from django.db import models

from django.db import models

class Skill(models.Model):
   
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
   
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']

class Profile(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    def __str__(self):
        return self.name
