from django.contrib import admin
from .models import Service_Fields, Service_Categories, Service_Tag,Cover, Why_Work

# Register your models here.


class Service_TagAdmin(admin.StackedInline):
    model = Service_Tag


@admin.register(Service_Categories)
class PostAdmin(admin.ModelAdmin):
    inlines = [Service_TagAdmin]

    class Meta:
       model = Service_Categories


@admin.register(Service_Tag)
class Service_TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cover)
admin.site.register(Service_Fields)
admin.site.register(Why_Work)
