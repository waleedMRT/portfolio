from django.shortcuts import render , redirect
from .models import ProfileImage , Project
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages


from django.shortcuts import render, redirect

def index_view(request):
    profile_img = ProfileImage.objects.last()
    projects = Project.objects.all()

    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['msg']
            try:
                send_mail(
                    subject=f'Message from {name}',
                    message=f'From: {email}\n\nMessage:\n{msg}',
                    from_email=None,
                    recipient_list=['merabetwalid15@gmail.com'],
                    fail_silently=False
                )
                messages.success(request, 'sent')
                return redirect('index')
            except Exception as e:
                messages.error(request, 'Try again.')
                print('Email error :' , e)

    context = {
        'profile_img': profile_img,
        'projects': projects,
        'form': form
    }
    return render(request, 'main/index.html', context)



    


def custom404(request , exception):
    return render(request , 'errors/404.html' , status=404)

def custom403(request):
    return render(request , 'errors/403.html' , status=403)
