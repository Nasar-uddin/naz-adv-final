from django.shortcuts import render
from .models import Service_Fields, Service_Categories, Service_Tag, Cover, Why_Work
from home.models import Brand
# Create your views here.


def service(request):
  brand = Brand.objects.all()[0]
  cover = Cover.objects.all()[0]
  service_fields = Service_Fields.objects.all()[:3]
  service_categories = Service_Categories.objects.all()[:6]
  service_tag = Service_Tag.objects.all()
  why_work = Why_Work.objects.all()[:3]

  context = {
    	'brand':brand,
      'cover': cover,
      'service_fields': service_fields,
      'service_categories': service_categories,
      'service_tag': service_tag,
      'why_work': why_work
  }
  return render(request, 'service/services.html', context)
