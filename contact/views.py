from django.shortcuts import render
from .models import ContactText
from home.models import Brand
# Create your views here.
def contact(request):
    brand = Brand.objects.all()[0]
    contactText = ContactText.objects.all()[0]
    contex = {
        'brand':brand,
        'contactText':contactText
    }
    return render(request,'contact/contact.html',contex)
