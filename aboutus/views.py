from django.shortcuts import render
from .models import *
from home.models import Brand
# Create your views here.
def aboutus(request):
    brand = Brand.objects.all()[0]
    about_us_text = AboutUs.objects.all()[0]
    plans = Plan.objects.all()[:3]
    mission = Mission.objects.all()[0]
    context = {
        'brand':brand,
        'about_us_text':about_us_text,
        'plans': plans,
        'mission':mission
    }
    return render(request,'aboutus/aboutus.html',context)