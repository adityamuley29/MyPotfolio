from django.shortcuts import render
from.models import Projects,Contact
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):

    projects = Projects.objects.all()

    if request.method == 'POST':
        # print(request)
        full_name = request.POST.get('full_name','')
        email = request.POST.get('email','')
        message = request.POST.get('message','')

        contact = Contact(full_name=full_name,email=email,message=message)
        # contact.save()

        send_mail(
            f"Email from {full_name}",
            f"New Mail From :- {email} \n \n Message :- {message}",
            settings.EMAIL_HOST_USER,
            ['adityamuley48@gmail.com'],
            fail_silently=False
        )
        
        


    return render(request,'index.html',{'projects':projects})
