from django.shortcuts import render, redirect, get_object_or_404
from app.forms import *
from app.models import *
from django.contrib import messages
# Create your views here.

def index(request):
    services = Service.objects.all()
    projects = Project.objects.all()
    context = {
        'services':services,
        'projects':projects,
    }
    return render(request, 'app/index.html', context)

def base(request):
    services = Service.objects.all()
    context = {
        'services':services
    }
    return render(request, 'app/base.html',context)

def base2(request):
    services = Service.objects.all()
    context = {
        'services':services
    }
    return render(request, 'app/base2.html',context)

def blog(request):
    x = Blog.objects.all()
    services = Service.objects.all()
    context = {
        'x':x,
        'services':services,
    }
    return render(request, 'app/blog.html',context)

def blog_detail(request,id):
    # Using get_object_or_404 ensures it returns a 404 error if the service doesn't exist
    x = get_object_or_404(Blog, id=id)
    services = Service.objects.all()
    
    context = {
        'x': x,
        'services':services
    }
    return render(request, 'app/blog_detail.html',context)



def gold_price(request):
    services = Service.objects.all()
    x = GoldPrice.objects.all()
    context = {
        'services':services,
        'x':x
    }
    return render(request, 'app/gold_price.html',context)


def projects(request):
    project = Project.objects.all()
    ongoingProject = Project.objects.filter(status='ongoing')
    completedProject = Project.objects.filter(status='completed')
    services = Service.objects.all()
    context = {
        'project':project,
        'services':services,
        'ongoingProject':ongoingProject,
        'completedProject':completedProject,
    }
    return render(request, 'app/projects.html',context)

def project_details(request,id):
    # Using get_object_or_404 ensures it returns a 404 error if the service doesn't exist
    project_detail = get_object_or_404(Project, id=id)
    services = Service.objects.all()
    project_images = ProjectImages.objects.filter(project=project_detail)
    
    context = {
        'project_detail': project_detail,
        'services':services,
        'project_images':project_images
    }
    return render(request, 'app/project_details.html',context)




def contact_us(request):
    services = Service.objects.all()
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for contacting us. Message sent successfully!')
            return redirect('contact_us')
    
    context = {
        'services':services,
        'form':form
    }
    return render(request, 'app/contact_us.html',context)

def company_overview(request):
    services = Service.objects.all()
    context = {
        'services':services
    }
    return render(request, 'app/company_overview.html',context)

def team(request):
    x = Team.objects.all()
    services = Service.objects.all()
    context = {
        'x':x,
        'services':services
    }
    return render(request, 'app/team.html',context)

def team_details(request,id):
    x = get_object_or_404(Team, id=id)
    services = Service.objects.all()
    
    context = {
        'x': x,
        'services':services
    }
    return render(request, 'app/team_details.html',context)



def services_details(request, id):
    # Using get_object_or_404 ensures it returns a 404 error if the service doesn't exist
    service_detail = get_object_or_404(Service, id=id)
    services = Service.objects.all()
    service_points = ServicePoint.objects.filter(service=service_detail)
    
    context = {
        'service_detail': service_detail,
        'services':services,
        'service_points':service_points,
    }
    return render(request, 'app/services_details.html', context)



def pdf_reader(request):
    return render(request, 'app/pdf_reader.html')

def messageSending(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # Message.success('message sent successfully')
                return redirect('index')
            except Exception as e:
                print({e})
        else:
            print('error upload')
    context = {
        'form':form
    }
    return render(request, 'app/index.html', context)