from collections import UserDict
from imaplib import _Authenticator
from pyexpat.errors import messages

from English_Website.settings import  LOGIN_REDIRECT_URL
from .forms import AddCommentForm, AddCourseForm, CommentForm, SignUpForm,SignUpForm1
from django.shortcuts import get_object_or_404, render, redirect 
from .forms import  AddFileForm, VideoForm
from .models import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import AuthenticationForm
from .forms import ContactForm,UserCreationForm,ContactPostForm,userPostForm,createCommentForm,AddHomeworkForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .filters import ArticleFilter


# Create your views here.

def index(request):
    return render(request, 'English_App/index.html')





@login_required(login_url='login')
def homepagetest(request):
    return render(request, 'English_App/homepagetest.html')


def logintest(request):
    return render(request, 'English_App/logintest.html')

@login_required(login_url='login')
def video(request):
    
    video = Video.objects.all()
    if request.method == "POST":
        form = VideoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_video')
    else:
        form=VideoForm()
    context = {'video_form':form,'video':video}
    
        
    return render(request,'English_App/video.html',context)

def news(request):
    return render(request,'English_App/news.html')


@login_required(login_url='login')
def add_file(request):
    files = AddFileModel.objects.all()
    if request.method == "POST":
        form = AddFileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'English_App/add_files.html')
            
    else:
        form=AddFileForm()
    context = {'addfileform':form,'files':files}
    
    
    return render(request, 'English_App/add_files.html',context)






def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'otmanelaaziz@hotmail.com', ['otmanelaaziz@hotmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("index")
      
	form = ContactForm()
	return render(request, "English_App/contact.html", {'form':form})






def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
             

           
            return redirect('login')
    else:
        form = UserRegistrationForm()

   

    context = {'form': form}
    return render(request, 'English_App/register.html', context)


@login_required(login_url='login')
def displaytable(request):
    users = User.objects.all()
    return render(request, 'English_App/display_users_list.html',{'users':users})


def displayContactInfo(request):
    form=ContactInfo.objects.all()

    return render(request,'English_App/displayContactInfo.html',{'contactinfo':form})


def del_user(request, username):    
    try:
        u = User.objects.get(username = username)
        u.delete()
        messages.sucess(request, "The user is deleted")
    except:
      messages.error(request, "The user not found")    
    return render(request, 'English_App/deleteUser.html',{'user':u})


def contactPost(request):
   
    if request.method == "POST":
        form =  ContactPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'English_App/contactpost.html')
            
    else:
        form= ContactPostForm()
    context = {'postform':form,}
    
    
    return render(request, 'English_App/contactpost.html',context)


def displayPostForms(request):
    posts = contactposts.objects.all()
    return render(request, 'English_App/display_posts_list.html',{'posts':posts})


def postUsers(request):
    usersposts = usersPosts.objects.all()
    if request.method == "POST":
        form =  userPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'English_App/userarticles.html')
            
    else:
        form= userPostForm()

    myFilter = ArticleFilter()
    context = {'userpostform':form,'usersposts':usersposts,'myFilter':myFilter}
    
    
    return render(request, 'English_App/userarticles.html',context)


def displayUsersArticaleList(request):
    userarticales=usersPosts.objects.all()
    return render(request,'English_App/userarticallist.html',{'usersposts':userarticales})

def updateUserArticle(request, id):

	updateuserarticale = usersPosts.objects.get(pk = id)
	form = userPostForm(instance=updateuserarticale)

	if request.method == 'POST':
		form = userPostForm(request.POST, instance=updateuserarticale)
		if form.is_valid():
			form.save()
			return redirect('index')

	context = {'form_update_article':form}
	return render(request, 'English_App/article_Update.html', context)

def articledetails(request,id):
    articledetails= get_object_or_404(usersPosts,pk=id)
   
    return render(request,'English_App/article_details.html',{'articledetails':articledetails})


# add comment def
def article_detail(request,id):
    template_name = 'article_details.html'
    post = get_object_or_404(usersPosts,pk=id)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = AddCommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = AddCommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

# end of it







def displayEachPosts(request,id):
    obj=get_object_or_404(usersPosts,pk=id)
    if request.method=="POST":
        obj.delete()
        return redirect ("postUsers")
    return render(request,'English_App/deletePost.html',{'obj':obj})

def deletePosts(request,id):
    obj=get_object_or_404(usersPosts,pk=id)
    if request.method=="POST":
        obj.delete()
        return redirect("index")
    return render(request,'English_App/deletePost.html',{'obj':obj})


def deleteUsers(request,id):
    deleteuser= get_object_or_404(User,pk=id)
    if request.method=="POST":
        deleteuser.delete()
        return redirect ("displaytable")
    return render(request,'English_App/deleteUser.html',{'deleteuser':deleteuser})


def updateUser(request, id):

	updateuser = User.objects.get(pk = id)
	form = UserRegistrationForm(instance=updateuser)

	if request.method == 'POST':
		form = UserRegistrationForm(request.POST, instance=updateuser)
		if form.is_valid():
			form.save()
			return redirect('index')

	context = {'form_update_user':form}
	return render(request, 'English_App/user_Update.html', context)





def AddCourse(request):
    
   
    if request.method == "POST":
        form =  AddCourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ("courseDetail")
            
    else:
        form= AddCourseForm()
    context = {'Add_Course':form}
    return render(request, 'English_App/Add_Courses.html',context)



def courseDetail(request):
    courses=AddCourseModel.objects.all()
    return render(request,'English_App/Courses_List.html',{'courses':courses})


def displayeachcourse(request,id):
    eachcourse= get_object_or_404(AddCourseModel,pk=id)
   
    return render(request,'English_App/course_detail.html',{'eachcourse':eachcourse})



class AddCommentView(CreateView):
    model = createComment
    template_name = 'Add_comment.html'
    fields = '__all__'



def deleteCourse(request,id):
    obj=get_object_or_404(AddCourseModel,pk=id)
    if request.method=="POST":
        obj.delete()
        return redirect("courseDetail")
    return render(request,'English_App/deleteCourse.html',{'deleteCourse':obj})


def deleteFile(request,id):
    obj=get_object_or_404(AddFileModel,pk=id)
    if request.method=="POST":
        obj.delete()
        return redirect("addfile")
    return render(request,'English_App/delete_File.html',{'deleteFile':obj})

def deleteVideo(request,id):
    obj=get_object_or_404(Video,pk=id)
    if request.method=="POST":
        obj.delete()
        return redirect("upload_video")
    return render(request,'English_App/delete_Video.html',{'deleteVideo':obj})


def filedetail(request,id):
    filedetail= get_object_or_404(AddFileModel,pk=id)

    return render(request,'English_App/file_detail.html',{'filedetail':filedetail})


def watchvideo(request,id):
    watchvideo= get_object_or_404(Video,pk=id)

    return render(request,'English_App/watchvideo.html',{'watchvideo':watchvideo})


def displayEachMessage(request,id):
    displayeachmessage= get_object_or_404(contactposts,pk=id)

    return render(request,'English_App/displayeachmessage.html',{'displayeachmessage':displayeachmessage})


def deleteMessages(request,id):
    deletemessage= get_object_or_404(contactposts,pk=id)
    if request.method=="POST":
        deletemessage.delete()
        return redirect ("displayPostForms")
    return render(request,'English_App/delete_Messages.html',{'deletemessage':deletemessage})


def CreateComments(request):
    comments = createComment.objects.all()
    if request.method == "POST":
        form =  createCommentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'English_App/Add_comment.html')
            
    else:
        form= createCommentForm()

    
    context = {'createcommentform':form,'comments':comments}

    return render(request, 'English_App/Add_comment.html',context)





def AddHomeworks(request):
    
  
    if request.method == "POST":
        form =  AddHomeworkForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ("index")
            
    else:
        form= AddHomeworkForm()
    context = {'Add_Homework':form}
    return render(request, 'English_App/Add_Homework.html',context)



def Homeworklist(request):
    homeworklist=AddHomework.objects.all()
  
    return render(request,'English_App/homework_List.html',{' homeworklist': homeworklist})


