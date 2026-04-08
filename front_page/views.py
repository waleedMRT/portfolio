from django.shortcuts import render , redirect
from .models import ProfileImage , Project
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
import threading
from django.conf import settings
import os
import requests

from django.shortcuts import render, redirect


def send_mail_async(name, email , msg):
    try:
        print("🚀 Sending via API...")

        response = requests.post(
            "https://api.sendgrid.com/v3/mail/send",
            headers={
                "Authorization": f"Bearer {settings.EMAIL_HOST_PASSWORD}",
                "Content-Type": "application/json"
            },
            json={
                "personalizations": [
                    {
                        "to": [{"email": "merabetwalid15@gmail.com"}]
                    }
                ],
                "from": {
                    "email": "merabetwalid15@gmail.com"
                },
                "subject": f"Message from {name}",
                "content": [
                    {
                        "type": "text/plain",
                        "value": f"Sender: {email}\n\nMessage:\n{msg}"
                    }
                ]
            }
        )

        print("Status:", response.status_code)

    except Exception as e:
        print("❌ Error:", e)


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
                    name , email , msg
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
