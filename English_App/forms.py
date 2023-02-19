from dataclasses import fields

from django import forms
import django
from django.forms import ModelForm, fields_for_model
from .models import   AddCourseModel, AddFileModel, ContactInfo, Video, contactposts,usersPosts,Comment,AddComment,createComment,AddHomework

from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

 
class SignUpForm1(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
class VideoForm(ModelForm):
	class Meta:
		model = Video
		fields = '__all__'



class AddFileForm(forms.ModelForm):
    class Meta:
        model = AddFileModel
        fields ='__all__'

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email','password1', 'password2')
        

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourseModel
        fields ='__all__'
   
        
     


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class ContactPostForm(forms.ModelForm):
    class Meta:
        model = contactposts
        fields ='__all__'

class userPostForm(forms.ModelForm):
    class Meta:
        model = usersPosts
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = AddComment
        fields = ('__all__')



class createCommentForm(forms.ModelForm):
    class Meta:
        model = createComment
        fields = ('__all__')


class AddHomeworkForm(forms.ModelForm):
    class Meta:
        model = AddHomework
        fields = ('__all__')

