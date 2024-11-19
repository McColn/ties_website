
from django.urls import path
from . import views
from .views import upload_project_image,upload_service_point

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('base2/', views.base2, name='base2'),
    path('blog/', views.blog, name='blog'),
    path('blogAdd/', views.blogAdd, name='blogAdd'),
    path('gold_price/', views.gold_price, name='gold_price'),
    path('blog_detail/<int:id>/', views.blog_detail, name='blog_detail'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:project_id>/upload-image/', upload_project_image, name='upload_project_image'),
    path('projectAdd/', views.projectAdd, name='projectAdd'),
    path('project/<int:id>/', views.project_details, name='project_details'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('company_overview/', views.company_overview, name='company_overview'),
    path('team/', views.team, name='team'),
    path('teamAdd/', views.teamAdd, name='teamAdd'),
    path('team_details/<int:id>/', views.team_details, name='team_details'),
    path('services/<int:id>/', views.services_details, name='services_details'),
    path('pdf_reader/', views.pdf_reader, name='pdf_reader'),
    path('messageSending/', views.messageSending, name='messageSending'),
    path('serviceAdd/', views.serviceAdd, name='serviceAdd'),
    path('service/<int:service_id>/upload-service/', upload_service_point, name='upload_service_point'),

]