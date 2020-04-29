from django.shortcuts import render
from .models import Service_Fields, Service_Categories, Service_Tag, Cover, Why_Work
# Create your views here.


def service(request):
  cover = Cover.objects.all()[0]
  service_fields = Service_Fields.objects.all()[:3]
  service_categories = Service_Categories.objects.all()[:6]
  service_tag = Service_Tag.objects.all()
  why_work = Why_Work.objects.all()[:3]

  context = {
      'cover': cover,
      'service_fields': service_fields,
      'service_categories': service_categories,
      'service_tag': service_tag,
      'why_work': why_work
  }
  return render(request, 'service/services.html', context)
