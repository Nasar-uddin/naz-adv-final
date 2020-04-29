
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('services/', include('service.urls')),
    path('contact/',include('contact.urls')),
    path('aboutus/',include('aboutus.urls')),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
