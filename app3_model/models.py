from django.db import models

# Create your frommodels here.
class Person(models.Model):
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=10,default='男')
    age = models.IntegerField()
    address = models.CharField(max_length=225,null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return self.name
class Course(models.Model):
    courseName = models.CharField(max_length=64)
    teacher = models.CharField(max_length=25)
    score = models.IntegerField()
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.courseName