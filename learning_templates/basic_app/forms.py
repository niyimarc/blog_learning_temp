from django import forms
from basic_app.models import Post
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        # __all__ will fetch all the form in the Post model in our models.py 
        fields = "__all__"

class RegForm(UserCreationForm):
    class Meta():
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email')

class EditUserForm(UserChangeForm):
    class Meta():
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email')