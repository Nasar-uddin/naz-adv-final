

from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
import service.views

urlpatterns = [
    path('', service.views.service, name='service'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
