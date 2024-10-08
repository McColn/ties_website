from django.shortcuts import render, redirect
from app.forms import *
from app.models import *
# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def base(request):
    return render(request, 'app/base.html')

def blog(request):
    return render(request, 'app/blog.html')

def blog_detail(request):
    return render(request, 'app/blog_detail.html')

def gold_price(request):
    return render(request, 'app/gold_price.html')


def projects(request):
    return render(request, 'app/projects.html')

def project_details(request):
    return render(request, 'app/project_details.html')

def contact_us(request):
    return render(request, 'app/contact_us.html')

def company_overview(request):
    return render(request, 'app/company_overview.html')

def team(request):
    return render(request, 'app/team.html')

def team_details(request):
    return render(request, 'app/team_details.html')

def services_details(request):
    return render(request, 'app/services_details.html')

def pdf_reader(request):
    return render(request, 'app/pdf_reader.html')