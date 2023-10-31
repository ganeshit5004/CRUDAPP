from django.contrib import admin
from secapp.models import student
# Register your models here.
class stud(admin.ModelAdmin):
    l=['sno','name','age','std']
admin.site.register(student,stud)

