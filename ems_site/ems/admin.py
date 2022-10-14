from pydoc import classify_class_attrs
from django.contrib import admin

from .models import Employee, Job
# Register your models here.
# admin.site.register(Employee)
# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'gender']

# @admin.register(Job)
# class JobAdmin(admin.ModelAdmin):
#     list_display =  ['name']


admin.site.register(Employee)