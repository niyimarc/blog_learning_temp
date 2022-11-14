from django.shortcuts import render, redirect
# import Post model from models 
from basic_app.models import Post
# import PostForm class created in forms.py 
from basic_app.forms import PostForm
# import ListView and DetailView  from django.views.generic 
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from basic_app.forms import PostForm, RegForm, EditUserForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
@login_required
def index(request):
    post = Post.objects.all()
    return render(request, 'basic_app/index.html', {"post": post})
def relative_url_templates(request):
    return render(request, 'basic_app/relative_url_templates.html')
def other(request):
    if request.method == "POST":
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            postform.save(commit=True)
            return redirect("home")
    else:
        postform = PostForm()
    return render(request, 'basic_app/other.html', {"postform": postform})

# the ListPost view will list out all the post 
class ListPost(ListView):
    model = Post
    template_name = 'basic_app/list_post.html'
    context_object_name = 'post_list'

# the DetailPost view will display the post based on the id of the post 
class DetailPost(DetailView):
    model = Post
    template_name = 'basic_app/detail_post.html'
    context_object_name = 'post_detail'

# the AddPost view will add to the Post model 
class AddPost(SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'basic_app/cbv_form.html'
    form_class = PostForm
    success_url = reverse_lazy('basic_app:add_post')
    success_message = 'Updated successfully'

# the UpdatePost view will update the Post model 
class UpdatePost(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'basic_app/cbv_form.html'
    form_class = PostForm
    success_url = reverse_lazy('basic_app:list_post')
    success_message = 'Updated successfully'

# the DeletePost view will delete the Post model 
class DeletePost(DeleteView):
    model = Post
    template_name = 'basic_app/confirm_delete.html'
    success_url = reverse_lazy('basic_app:list_post')

def register(request):
    if request.method == "POST":
        regform = RegForm(request.POST)
        if regform.is_valid():
            regform.save(commit=True)
            return redirect("home")
    else:
        regform = RegForm()
    return render(request, 'basic_app/register.html', {"regform": regform})

def edit_form(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'User edited successfully')
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'basic_app/edit_form.html', {"edit_key": edit_form})

def pass_form(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST, user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            messages.success(request, 'Password changed successfully')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'basic_app/pass_form.html', {"pass_key": pass_form})