from django.db import models
from django.contrib.auth.models import User
from django.urls import  reverse
from datetime import datetime,date

# Create your models here.


class Department(models.Model):
   dept_name = models.CharField(max_length=30, blank=False)

   def __str__(self):
      return self.dept_name

    #after creating ! new data will pops up in specific page !
   def get_absolute_url(self):
      return reverse('home_link')


class Students(models.Model):

   author = models.ForeignKey(User,on_delete=models.CASCADE)
   #------------------------------------------------------
   name = models.CharField(max_length=30, blank=False)
   student_id = models.CharField(max_length=30, blank=False)
   phone_number = models.CharField(max_length=30,blank=False)
   email =models.EmailField(max_length=30,blank=False)

   student_profile_image = models.ImageField(null=True,blank=True,upload_to='profile_image/')

   student_add_data = models.DateField(auto_now_add=True)
   student_address = models.CharField(max_length=40,default="no address")

   student_department = models.CharField(max_length=30,default="uncategorized")

   local_guardian_name = models.CharField(max_length=40,default="no address")
   local_guardian_address= models.CharField(max_length=40,default="no address")
   local_guardian_phone= models.CharField(max_length=40,default="no address")






   class Meta:
      ordering = ['-id']




   def __str__(self):
      return self.name + ' | ' + str(self.author)+' | '+ str(self.pk)

    #after creating ! new data will pops up in specific page !
   def get_absolute_url(self):
      return reverse('profile_view_with_class_link',args=[str(self.id)])




    #after creating ! new data will pops up in specific page !


