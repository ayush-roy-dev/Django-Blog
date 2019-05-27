from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog_home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('about/', views.about, name='blog_about'),
]
