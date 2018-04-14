from django.contrib import admin
from .models import Person,Course

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','sex','age','address','email')
class courseAdmin(admin.ModelAdmin):
    list_display = ('courseName','teacher','score','name')
admin.site.register(Person,PersonAdmin)
admin.site.register(Course,courseAdmin)