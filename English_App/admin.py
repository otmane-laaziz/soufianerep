from django.contrib import admin



# Register your models here.


from .models import *

admin.site.register(Video)
admin.site.register(contactposts)
admin.site.register(usersPosts)

admin.site.register(AddCourseModel)
admin.site.register(createComment)
admin.site.register(AddHomework)



