from django.shortcuts import render, redirect, get_object_or_404
from app.models import *
from app.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    Messages_count = Message.objects.count()
    team_count = Team.objects.count()
    service_count = Service.objects.count()
    blog_count = Blog.objects.count()
    # Count ongoing projects
    ongoing_count = Project.objects.filter(status='ongoing').count()
    # Count completed projects
    completed_count = Project.objects.filter(status='completed').count()
    context = {
        'Messages_count': Messages_count,
        'team_count': team_count,
        'service_count': service_count,
        'blog_count': blog_count,
        'ongoing_count': ongoing_count,
        'completed_count': completed_count
    }
    return render(request, 'administrator/home.html',context)

@login_required
def base3(request):
    return render(request, 'administrator/base3.html')

@login_required
def blog2(request):
    x = Blog.objects.all()
    context = {
        'x': x
    }
    return render(request, 'administrator/blog2.html',context)

@login_required
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
    return render(request, 'administrator/blogAdd.html', context)

@login_required
def blogEdit(request,id):
    s = get_object_or_404(Blog, id=id)
    form = BlogForm(instance=s)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=s)
        if form.is_valid():
            form.save()
            return redirect('blog2')
    context={
        'form':form,
        's':s,
        'title': s.title
    }
    return render(request, 'administrator/blogEdit.html',context)

@login_required
def blogDelete(request,id):
    x = get_object_or_404(Blog,id=id)
    x.delete()
    return redirect('blog2')

@login_required
def messages(request):
    message = Message.objects.all().order_by('-id')
    context = {
        'message': message
    }
    return render(request, 'administrator/messages.html', context)

@login_required
def deleteMessage(request,id):
    x = get_object_or_404(Message,id=id)
    x.delete()
    return redirect('messages')

@login_required
def team2(request):
    team = Team.objects.all().order_by('-id')
    context = {
        'team': team
    }
    return render(request, 'administrator/team2.html', context)

@login_required
def teamAdd(request):
    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team2')
    context={
        'form':form
    }
    return render(request, 'administrator/teamAdd.html',context)

@login_required
def teamEdit(request,id):
    s = get_object_or_404(Team, id=id)
    form = TeamForm(instance=s)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=s)
        if form.is_valid():
            form.save()
            return redirect('team2')
    context={
        'form':form,
        's':s,
        'profile': s.profile
    }
    return render(request, 'administrator/teamEdit.html',context)

@login_required
def deleteTeamMember(request,id):
    x = get_object_or_404(Team,id=id)
    x.delete()
    return redirect('team2')

@login_required
def projects2(request):
    project = Project.objects.all().order_by('-id')
    context = {
        'project': project
    }
    return render(request, 'administrator/projects2.html', context)

@login_required
def projectAdd(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects2')
    context={
        'form':form
    }
    return render(request, 'administrator/projectAdd.html',context)

@login_required
def projectDetails(request,id):
    s = get_object_or_404(Project, id=id)
    project_images = ProjectImages.objects.filter(project=s)
    context = {
        's': s,
        'project_images': project_images
    }
    return render(request, 'administrator/projectDetails.html', context)

@login_required
def projectEdit(request,id):
    s = get_object_or_404(Project, id=id)
    form = ProjectForm(instance=s)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=s)
        if form.is_valid():
            form.save()
            return redirect('projectDetails',id=id)
    context={
        'form':form,
        's':s,
        'body': s.body
    }
    return render(request, 'administrator/projectEdit.html',context)

@login_required
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
            return redirect('projectDetails', id=project.id)

    else:
        # Display an empty form for image upload
        form = ProjectImagesForm()

    # Render the upload form in the template
    return render(request, 'administrator/upload_project_image.html', {'form': form, 'project': project})

@login_required
def services(request):
    service = Service.objects.all().order_by('-id')
    context = {
        'service': service
    }
    return render(request, 'administrator/services.html', context)

@login_required
def serviceAdd(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services')
    context={
        'form':form
    }
    return render(request, 'administrator/serviceAdd.html',context)

@login_required
def serviceDetails(request, id):
    # Using get_object_or_404 ensures it returns a 404 error if the service doesn't exist
    service_detail = get_object_or_404(Service, id=id)
    services = Service.objects.all()
    service_points = ServicePoint.objects.filter(service=service_detail)
    
    context = {
        'service_detail': service_detail,
        'services':services,
        'service_points':service_points,
    }
    return render(request, 'administrator/serviceDetails.html', context)

@login_required
def serviceEdit(request,id):
    s = get_object_or_404(Service, id=id)
    form = ServiceForm(instance=s)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=s)
        if form.is_valid():
            form.save()
            return redirect('serviceDetails',id=id)
    context={
        'form':form,
        's':s,
        'body': s.body
    }
    return render(request, 'administrator/serviceEdit.html',context)

@login_required
def serviceSubtaskAdd(request, service_id):
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
            return redirect('serviceDetails', id=service.id)

    else:
        # Display an empty form for image upload
        form = ServicePointForm()

    # Render the upload form in the template
    return render(request, 'administrator/serviceSubtaskAdd.html', {'form': form, 'service': service})

@login_required
def deleteServiceSubtask(request,id):
    x = get_object_or_404(ServicePoint,id=id)
    x.delete()
    return redirect('services')

@login_required
def deleteService(request,id):
    x = get_object_or_404(Service,id=id)
    x.delete()
    return redirect('services')

@login_required
def goldPrice(request):
    x = GoldPrice.objects.order_by('-id').first()
    context = {
        'x': x
    }
    return render(request, 'administrator/goldPrice.html', context)

@login_required
def goldPriceAdd(request):
    form = GoldPriceForm()
    if request.method == 'POST':
        form = GoldPriceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('goldPrice')
    context={
        'form':form
    }
    return render(request, 'administrator/goldPriceAdd.html',context)

@login_required
def goldPriceEdit(request,id):
    s = get_object_or_404(GoldPrice, id=id)
    form = GoldPriceForm(instance=s)
    if request.method == 'POST':
        form = GoldPriceForm(request.POST, request.FILES, instance=s)
        if form.is_valid():
            form.save()
            return redirect('goldPrice')
    context={
        'form':form,
        's':s,
    }
    return render(request, 'administrator/goldPriceEdit.html',context)

def custom_logout_view(request):
    logout(request)
    return redirect('index') 

def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate (username=username,password = password1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('signin')
    return render(request, 'administrator/signin.html')