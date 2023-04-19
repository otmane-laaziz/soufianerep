from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms
from .validators import file_size
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.fields import RichTextField



# Create your models here.
class Video(models.Model):
    
    caption = models.CharField(max_length=500)
    
    video = models.FileField(upload_to="video/%y",validators=[file_size])
    
    

    def __str__(self):
        return self.caption



class AddFileModel(models.Model):
   
    title = models.CharField(max_length = 80)
    pdf = models.FileField(upload_to='pdfs/%y')
 
    class Meta:
        ordering = ['title']
     
    def __str__(self):
        return f"{self.title}"





class UserRegistrationForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



  


class ContactInfo(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email_address = models.EmailField(max_length = 150)
    message = models.CharField(max_length = 2000)



class contactposts(models.Model):
    
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email_address = models.CharField(max_length = 150)
    phone_number = models.CharField(max_length = 50)
    body = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.first_name +'|'+ str(self.last_name)
   
      


class usersPosts(models.Model):
    
    title = models.CharField(max_length = 50)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    def __str__(self):
        return self.title +'|' + str(self.author)


class AddCourseModel(models.Model):
    
    courseName = models.CharField(max_length = 50)
    courseBody = RichTextField(blank=True,null=True)
    #courseBody = models.TextField()
    def __str__(self):
        return self.courseName

# this model not good
class Comment(models.Model):
    user = models.CharField(max_length = 50)
    date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=80)
    content = models.TextField()
    def __str__(self):
        return '%s - %s' % (self.post.title,self.user)


class AddComment(models.Model):
    posts = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

   

  

  #end of it

class createComment(models.Model):
    
    articles = models.ForeignKey(usersPosts, related_name="ourcomments",on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class AddHomework(models.Model):
    
    homeworkname = models.CharField(max_length=80)
    topic = RichTextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

  
   





