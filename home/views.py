from django.shortcuts import render,get_object_or_404
from .models import Slider, Service_Header, Service_Body, Projects, ProjectsImage,Category, ClientQuote, ClientBrand, Business, Technique, Technique_Info,Brand

# Create your views here.
def home(request):
  brand = Brand.objects.all()[0]
  slider=Slider.objects.all()
  service_header = Service_Header.objects.all()[0]
  service_body = Service_Body.objects.all()[:3]
  projects = Projects.objects.all()[:8]
  clientquote = ClientQuote.objects.all()[0]
  clientbrand = ClientBrand.objects.all()
  business = Business.objects.all()[0]
  technique = Technique.objects.all()[:4]
  technique_info = Technique_Info.objects.all()[0]
 
  context={
    'brand':brand,
    'slider':slider,
    'service_header':service_header,
    'service_body':service_body,
    'projects':projects,
    'clientquote':clientquote,
    'clientbrand':clientbrand,
    'business':business,
    'technique':technique,
    'technique_info':technique_info
  }
  return render(request,'home/index.html',context)

def project_detail(request,category,id):
  brand = Brand.objects.all()[0]
  project=get_object_or_404(Projects,id=id)
  photos = ProjectsImage.objects.filter(projects=project)
  cat = get_object_or_404(Category, name=category)
  projects = Projects.objects.filter(category=cat.id)
  print(projects)
  context={
    'brand':brand,
    'project':project,
    'photos':photos,
    'projects':projects
  }
  return render(request, 'home/project_detail.html', context)
