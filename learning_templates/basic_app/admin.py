from django.contrib import admin
# import the UserProfile from the models in basic_app 
from basic_app.models import UserProfile, Post, Category

# Register your models here.
# register the UserProfile model 
admin.site.register(UserProfile)
# register the Post model 
admin.site.register(Post)
# register the Category model 
admin.site.register(Category)