from django.shortcuts import render, redirect, get_object_or_404
from app.forms import *
from app.models import *
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

def blogAdd(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                leave = form.save(commit=False)
                leave.uploader = request.user  # Assigning the uploader
                leave.save()
                return redirect('blog')
            except Exception as e:
                print(f"Error updating item: {e}")
                print(f"Username: {request.user.username}")
        else:
            print("Form is not valid")
    context = {
        'form': form
    }
    return render(request, 'app/blogAdd.html', context)

def gold_price(request):
    services = Service.objects.all()
    context = {
        'services':services
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

def upload_project_image(request, project_id):
    # Get the specific project by its ID or return a 404 error if not found
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        # Process the form submission
        form = ProjectImagesForm(request.POST, request.FILES)
        if form.is_valid():
            project_image = form.save(commit=False)
            project_image.project = project  # Associate the image with the specific project
            project_image.save()
            # return redirect('project_details', project_id=project.id)
            return redirect('project_details', id=project.id)

    else:
        # Display an empty form for image upload
        form = ProjectImagesForm()

    # Render the upload form in the template
    return render(request, 'app/project_details.html', {'form': form, 'project': project})


def contact_us(request):
    services = Service.objects.all()
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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

def teamAdd(request):
    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team')
    context={
        'form':form
    }
    return render(request, 'app/teamAdd.html',context)

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



def serviceAdd(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('serviceAdd')
    context={
        'form':form
    }
    return render(request, 'app/serviceAdd.html',context)

def upload_service_point(request, service_id):
    # Get the specific project by its ID or return a 404 error if not found
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        # Process the form submission
        form = ServicePointForm(request.POST, request.FILES)
        if form.is_valid():
            service_image = form.save(commit=False)
            service_image.service = service  # Associate the image with the specific service
            service_image.save()
            # return redirect('project_details', service_id=project.id)
            return redirect('services_details', id=service.id)

    else:
        # Display an empty form for image upload
        form = ServicePointForm()

    # Render the upload form in the template
    return render(request, 'app/services_details.html', {'form': form, 'service': service})



def projectAdd(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projectAdd')
    context={
        'form':form
    }
    return render(request, 'app/projectAdd.html',context)


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