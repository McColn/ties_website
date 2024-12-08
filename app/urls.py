
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('base2/', views.base2, name='base2'),
    path('blog/', views.blog, name='blog'),
    path('gold_price/', views.gold_price, name='gold_price'),
    path('blog_detail/<int:id>/', views.blog_detail, name='blog_detail'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:id>/', views.project_details, name='project_details'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('company_overview/', views.company_overview, name='company_overview'),
    path('team/', views.team, name='team'),
    path('team_details/<int:id>/', views.team_details, name='team_details'),
    path('services/<int:id>/', views.services_details, name='services_details'),
    path('pdf_reader/', views.pdf_reader, name='pdf_reader'),
    path('messageSending/', views.messageSending, name='messageSending'),

]