from django.contrib import admin
from app.models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Message)
admin.site.register(Project)
admin.site.register(ProjectImages)
admin.site.register(Blog)
admin.site.register(GoldPrice)
admin.site.register(Service)
admin.site.register(Team)
admin.site.register(ServicePoint)