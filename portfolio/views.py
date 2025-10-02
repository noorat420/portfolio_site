from django.shortcuts import render, get_object_or_404
from .models import Project, Skill, Profile

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