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

class Experience(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Certification(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, blank=True)
    issue_date = models.DateField(blank=True, null=True)
    credential_link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=200)
    provider = models.CharField(max_length=200, blank=True)
    completion_date = models.DateField(blank=True, null=True)
   

    def __str__(self):
        return self.name  
    
