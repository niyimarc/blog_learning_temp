from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    age = models.IntegerField()
    website = models.URLField(null= True, blank = True)
    def __str__(self):
        return self.user.username

# Create the post category model 
class Category(models.Model):
    cat_name = models.CharField(verbose_name='Category Name', max_length=100)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    def __str__(self):
        return self.cat_name

# Create the post model 
class Post(models.Model):
    post_title = models.CharField(max_length = 150, verbose_name ='Post Title')
    category = models.ForeignKey(Category, on_delete =models.CASCADE, verbose_name = 'Post Category')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Author')
    post_img = models.ImageField(blank=True, null=True, verbose_name= 'Post Image')
    create_date = models.DateTimeField(default=timezone.now)
    contents = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.post_title
