from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage

from .models import Post
from .forms import PostForm, ContactForm, UploadForm

def index(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'web/index.html', context)    

def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'web/detail.html', {'post':post})

def about(request):
    return HttpResponse("About Page")

def contact(request):
    if request.method == "POST":
        
        subject = request.POST.get('subject','')
        from_email = request.POST.get('from_email','')
        description = request.POST.get('description','')

        send_mail(
            subject,
            description,
            from_email,
            ['absaralam2014@gmail.com'],
            fail_silently=False,
        )
        return redirect('web:contact')
    else:
        form = ContactForm()
    return render(request, 'web/contact.html', {'form':form})

@login_required
def new_post(request):
    if request.method == 'POST':
        data = PostForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            return redirect('web:index')
    else:
        form = PostForm()
    return render(request, 'web/new_post.html', {'form':form})

def upload_file(request):
    if request.method == "POST":
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        return redirect('web:upload_file')
    else:
        form = UploadForm()
    return render(request, 'web/upload_file.html', {'form':form})