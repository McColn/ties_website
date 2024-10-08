
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('blog/', views.blog, name='blog'),
    path('gold_price/', views.gold_price, name='gold_price'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('projects/', views.projects, name='projects'),
    path('project_details/', views.project_details, name='project_details'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('company_overview/', views.company_overview, name='company_overview'),
    path('team/', views.team, name='team'),
    path('team_details/', views.team_details, name='team_details'),
    path('services_details/', views.services_details, name='services_details'),
    path('pdf_reader/', views.pdf_reader, name='pdf_reader'),
]