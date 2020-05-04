from django.contrib import admin
from .models import Slider,Service_Header,Service_Body,Projects,ProjectsImage,Category,ClientQuote,ClientBrand,Business,Technique,Technique_Info,Brand

# Register your models here.


class ProjectsImageAdmin(admin.StackedInline):
    model = ProjectsImage


@admin.register(Projects)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProjectsImageAdmin]

    class Meta:
       model = Projects


@admin.register(ProjectsImage)
class ProjectsImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Brand)
admin.site.register(Slider)
admin.site.register(Service_Header)
admin.site.register(Service_Body)
admin.site.register(Category)
admin.site.register(ClientQuote)
admin.site.register(ClientBrand)
admin.site.register(Business)
admin.site.register(Technique)
admin.site.register(Technique_Info)
