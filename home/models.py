from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=250)
  email = models.EmailField(max_length=254)
  massage = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
			return self.name

class Branch(models.Models):
  branch = models.CharField( max_length=50)
  created_Date=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.branch
 
class Teacher(models.Model):
  
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    phone_teacher = models.CharField( max_length=100)
    email_teacher = models.EmailField(max_length=254)
    speciality = models.ForeignKey(Branch, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="teacher", default="default.png")
    
    updatedDate = models.DateTimeField(auto_now=True)
    createdDate=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.first_name+ " " +self.last_name
      

