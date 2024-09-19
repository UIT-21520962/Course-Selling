from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    id = models.CharField(max_length=20, primary_key=True, null=False)
    name = models.CharField(max_length=200, null=True)
    price= models.FloatField()
    image = models.ImageField(null=True, blank=True)
    video = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def ImageURL(self):
        try: 
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True) 
    dateorder = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
   
    def __str__(self):
        return str(self.id)
    
class CourseOrder(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True) 
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True) 
    date_added = models.DateTimeField(auto_now_add=True)


    