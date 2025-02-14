from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.Blogs, name='blog_list'),
    # path('blog/', views.BlogListView.as_view(), name='blog_list'),
    # path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_list'),
    path('contact/', views.contact, name='contact'),
]
