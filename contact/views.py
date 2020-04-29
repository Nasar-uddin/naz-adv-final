from django.shortcuts import render
from .models import ContactText
# Create your views here.
def contact(request):
    contactText = ContactText.objects.all()[0]
    contex = {
        'contactText':contactText
    }
    return render(request,'contact/contact.html',contex)
