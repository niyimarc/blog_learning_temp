from django.urls import path
from basic_app import views
from django.contrib.auth import views as auth_views


app_name = 'basic_app'

urlpatterns = [
    path("other/", views.other, name = "other"),
    path("relative_url_templates/", views.relative_url_templates, name = "relative_url_templates"),
    path("list_post", views.ListPost.as_view(), name = "list_post"),
    # <int:pk> will fetch the post with the primary key 
    path("post_detail/<int:pk>", views.DetailPost.as_view(), name = "post_detail"),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('update/<int:pk>', views.UpdatePost.as_view(), name='update_post'),
    path('delete_post/<int:pk>', views.DeletePost.as_view(), name='delete_post'),
    path('register/', views.register, name='register'),
    path('login_page/', auth_views.LoginView.as_view(template_name= 'basic_app/login.html'), name='login'),
    path('logout_page/', auth_views.LogoutView.as_view(template_name= 'basic_app/logout.html'), name='logout'),
    path('edit_form_page/', views.edit_form, name='edit_form'),
    path('pass_form_page/', views.pass_form, name='pass_form'),
]