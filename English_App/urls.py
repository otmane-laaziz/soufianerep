from django.urls import path


from English_App import views as user_views
from . import views


urlpatterns = [
 path('', views.index, name="index"),
 path('upload_video', views.video, name="upload_video"),
 path('news', views.news, name="news"),
 path('addfile', views.add_file, name ='addfile'),
 
 
  
path("contact", views.contact, name="contact"),


path('register/', user_views.register, name='register'),
path('displaytable/', user_views.displaytable, name='displaytable'),
path('displayContactInfo/', user_views.displayContactInfo, name='displayContactInfo'),
path('contactPost/', user_views.contactPost, name='contactPost'),
path('displayPostForms/', user_views.displayPostForms, name='displayPostForms'),

path('postUsers/', user_views.postUsers, name='postUsers'),
path('<int:id>', user_views.displayEachPosts, name='displayEachPosts'),
path('<int:id>', user_views.deletePosts, name='deletePosts'),
path('deleteUsers/<int:id>', user_views.deleteUsers, name='deleteUsers'),
path('updateUser/<int:id>', user_views.updateUser, name='updateUser'),
path('filedetail/<int:id>', user_views.filedetail, name='filedetail'),
path('displayUsersArticaleList/', user_views.displayUsersArticaleList, name='displayUsersArticaleList'),
path('updateUserArticle/<int:id>', user_views.updateUserArticle, name='updateUserArticle'),
path('articledetails/<int:id>', user_views.articledetails, name='articledetails'),
path('AddCourse/', user_views.AddCourse, name='AddCourse'),
path('courseDetail/', user_views.courseDetail, name='courseDetail'),
path('displayeachcourse/<int:id>', user_views.displayeachcourse, name='displayeachcourse'),
path('article_detail/<int:id>', views.article_detail, name='article_detail'),
path('deleteCourse/<int:id>', user_views.deleteCourse, name='deleteCourse'),
path('deleteFile/<int:id>', user_views.deleteFile, name='deleteFile'),
path('deleteVideo/<int:id>', user_views.deleteVideo, name='deleteVideo'),
path('watchvideo/<int:id>', user_views.watchvideo, name='watchvideo'),
path('displayEachMessage/<int:id>', user_views.displayEachMessage, name='displayEachMessage'),
path('deleteMessages/<int:id>', user_views.deleteMessages, name='deleteMessages'),
path('CreateComments/', user_views.CreateComments, name='CreateComments'),
path('AddHomeworks/', user_views.AddHomeworks, name='AddHomeworks'),


path('Homeworklist/', user_views.Homeworklist, name='Homeworklist'),











 
 
 
]
