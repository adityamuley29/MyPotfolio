from django.shortcuts import render
from.models import Projects,Contact

# Create your views here.
def home(request):

    projects = Projects.objects.all()

    if request.method == 'POST':
        # print(request)
        full_name = request.POST.get('full_name','')
        email = request.POST.get('email','')
        message = request.POST.get('message','')

        contact = Contact(full_name=full_name,email=email,message=message)
        contact.save()
        
        


    return render(request,'index.html',{'projects':projects})
