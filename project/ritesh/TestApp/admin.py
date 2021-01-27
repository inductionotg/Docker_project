from django.contrib import admin
from TestApp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','eaddr']

admin.site.register(Employee,EmployeeAdmin)