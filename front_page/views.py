from django.shortcuts import render , redirect
from .models import ProfileImage , Project
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
import threading


from django.shortcuts import render, redirect


def send_mail_async(subject , message , recipient_list):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=None,
            recipient_list=recipient_list,
            fail_silently=False
        )
    except Exception as e:
        print('Erro email : ' , e)


def index_view(request):
    profile_img = ProfileImage.objects.last()
    projects = Project.objects.all()

    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['msg']
            

            thread = threading.Thread(
                target=send_mail_async,
                args=(
                    f'Message from {name}',
                    f'From {email}\n\nMessage:\n{msg}',
                    ['merabetwalid15@gmail.com']
                )
            )
            thread.start()
            messages.success(request , 'sent')
            return redirect('index')

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
