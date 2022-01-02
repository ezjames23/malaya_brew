from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html', {})



def contact(request):
    if request.method == "POST":
        lname = request.POST['contact_name']
        email = request.POST['contact_email']
        subject = request.POST['contact_subject']
        message = request.POST['contact_message']

        # send an email

        send_mail(
            'Malaya Brew Order from ' + lname, # subject
            message, #subject
            email, # from email
            ['malayabrew@gmail.com'], # to email

            )

        return render(request, 'contact.html', {'lname': lname})



    else:
        return render(request, 'contact.html', {})


    
def menu(request):
    return render(request, 'menu.html', {})


def today(request):
    return render(request, 'today-special.html', {})


    