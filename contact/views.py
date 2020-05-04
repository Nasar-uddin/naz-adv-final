from django.shortcuts import render
from .models import ContactText,Contacts
from home.models import Brand
# Create your views here.
def contact(request):
    brand = Brand.objects.all()[0]
    contacts = Contacts.objects.all()[0]
    contactText = ContactText.objects.all()[0]
    contex = {
        'brand':brand,
        'contacts':contacts,
        'contactText':contactText
    }
    return render(request,'contact/contact.html',contex)
