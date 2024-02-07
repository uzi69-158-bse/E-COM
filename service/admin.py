from django.contrib import admin
from service.models import dynamicService

# Register your models here.
class dynamicServiceadmin(admin.ModelAdmin):
    list_display =['service_icon','service_name','service_description']

admin.site.register(dynamicService,dynamicServiceadmin)    
