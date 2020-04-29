
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
import portfolio.views

urlpatterns = [
    path('',portfolio.views.portfolio,name='portfolio'),
    path('<category>/<int:id>/',portfolio.views.project_detail, name='project_detail'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
