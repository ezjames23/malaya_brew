from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})



def contact(request):
    if request.method == "POST":
        lname = request.POST['contact_name']
        email = request.POST['contact_email']
        subject = request.POST['contact_subject']
        message = request.POST['contact_message']

        return render(request, 'contact.html', {'lname': lname})



    else:
        return render(request, 'contact.html', {})