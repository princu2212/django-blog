from django.urls import path

from . import views

app_name = "web"
urlpatterns  = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('details/<post_id>', views.detail, name='detail'),
    path('new_post', views.new_post, name='new_post'),
    path('upload_file', views.upload_file, name='upload_file'),
]