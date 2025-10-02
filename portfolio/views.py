from django.shortcuts import render, get_object_or_404
from .models import Project, Skill, Profile,Experience, Education, Certification, Course

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    
    context = {
        'profile': profile,
        'skills': skills,
    }
    return render(request, 'portfolio/home.html', context)

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': all_projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def contact(request):
   
    return render(request, 'portfolio/contact.html')    



def about(request):
    
    profile = Profile.objects.first()
    experiences = Experience.objects.all() 
    educations = Education.objects.all() 
    certifications = Certification.objects.all() 
    courses = Course.objects.all() 

    context = {
        'profile': profile,
        'experiences': experiences,
        'educations': educations,
        'certifications': certifications,
        'courses': courses,
    }

    return render(request, 'portfolio/about.html', context)