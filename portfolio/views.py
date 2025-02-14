from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Skill, Education, Experience, Project, BlogPost, Certification
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


# Create your views here.

def home(request):
    return render(request, 'portfolio/index.html')
    # return HttpResponse("Hello World")


def about(request):
    context = {
        'skills': Skill.objects.all(),
        'education': Education.objects.all(),
        'experience': Experience.objects.all(),
        'certifications': Certification.objects.all().order_by('-date_issued')
    }
    return render(request, 'portfolio/about.html', context)


def projects(request):
    category = request.GET.get('category')
    projects = Project.objects.all()

    if category:
        projects = projects.filter(category=category)

    return render(request, 'portfolio/projects.html', {'projects': projects})

def Blogs(request):
    posts = BlogPost.objects.all()
    context= {'posts': posts}
    return render(request, 'portfolio/blog_list.html', context)


# class BlogListView(ListView):
#     model = BlogPost
#     template_name = 'blog_list.html'
#     context_object_name = 'posts'
#     queryset = BlogPost.objects.filter(is_published=True)
#     paginate_by = 5

# class BlogDetailView(DetailView):
#     model = BlogPost
#     template_name = 'blog_list.html'
#     context_object_name = 'post'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            send_mail(
                subject=form.cleaned_data['subject'],
                message=f"From: {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n{form.cleaned_data['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
            )
            return render(request, 'portfolio/contact_success.html')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/contact.html', {'form': form})
