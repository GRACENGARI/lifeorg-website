from django.shortcuts import render,redirect
from .models import Contact
from .serializer import ContactSerializer
from rest_framework  import viewsets



class Contactviewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer    
# Create your views here.
def index(request):
    return render(request, 'index.html')




def portfolio(request):
    return render(request, 'portfolio.html')


def starter(request):
    return render(request, 'starter.html')

def service(request):
    return render(request, 'service.html')




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        return redirect('index')  # Redirect to the index page after saving the contact

    return render(request, 'index.html')