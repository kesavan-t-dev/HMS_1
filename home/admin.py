from django.contrib import admin 
  
# Register your models here. 
from .models import doctors,slots,patients,mapping
  
admin.site.register(doctors)
admin.site.register(slots)
admin.site.register(patients)
admin.site.register(mapping)