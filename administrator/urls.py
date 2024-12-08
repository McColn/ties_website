
from django.urls import path
from .import views
from .views import custom_logout_view

urlpatterns = [
    path('home/', views.home, name='home'),
    path('base3/', views.base3, name='base3'),
    path('blog2/', views.blog2, name='blog2'),
    path('blogAdd/', views.blogAdd, name='blogAdd'),
    path('blogDelete/<int:id>/', views.blogDelete, name='blogDelete'),
    path('blogEdit/<int:id>/', views.blogEdit, name='blogEdit'),
    path('messages/', views.messages, name='messages'),
    path('deleteMessage/<int:id>/', views.deleteMessage, name='deleteMessage'),
    path('team2/', views.team2, name='team2'),
    path('teamAdd/', views.teamAdd, name='teamAdd'),
    path('deleteTeamMember/<int:id>/', views.deleteTeamMember, name='deleteTeamMember'),
    path('teamEdit/<int:id>/', views.teamEdit, name='teamEdit'),
    path('projectDetails/<int:id>/', views.projectDetails, name='projectDetails'),
    path('projectEdit/<int:id>/', views.projectEdit, name='projectEdit'),
    path('upload_project_image/<int:project_id>/', views.upload_project_image, name='upload_project_image'),
    path('projects2/', views.projects2, name='projects2'),
    path('projectAdd/', views.projectAdd, name='projectAdd'),
    path('services/', views.services, name='services'),
    path('serviceAdd/', views.serviceAdd, name='serviceAdd'),
    path('serviceDetails/<int:id>/', views.serviceDetails, name='serviceDetails'),
    path('serviceEdit/<int:id>/', views.serviceEdit, name='serviceEdit'),
    path('deleteService/<int:id>/', views.deleteService, name='deleteService'),
    path('deleteServiceSubtask/<int:id>/', views.deleteServiceSubtask, name='deleteServiceSubtask'),
    path('serviceSubtaskAdd/<int:service_id>/', views.serviceSubtaskAdd, name='serviceSubtaskAdd'),

    path('goldPrice/', views.goldPrice, name='goldPrice'),
    path('goldPriceAdd/', views.goldPriceAdd, name='goldPriceAdd'),
    path('goldPriceEdit/<int:id>/', views.goldPriceEdit, name='goldPriceEdit'),

    path('logout/', custom_logout_view, name='logout'),
    path('', views.signin, name='signin'),

]