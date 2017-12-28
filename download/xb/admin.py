from django.contrib import admin
from django.template import loader
from django.http import HttpResponse
from .models import Thread, Image
from .download import update_images

def print_images(modeladmin, request, queryset):
    template = loader.get_template('images.html')
    images = None
    if queryset.count() >= 1:
        images = Image.objects.filter(thread=queryset[0])
    return HttpResponse(template.render({'images': images}, request));
print_images.short_description = 'Show Images'

def download_images(modeladmin, request, queryset):
    template = loader.get_template('download.html')
    if queryset.count() >= 1:
        update_images(queryset[0])
    return HttpResponse(template.render({}, request));
download_images.short_description = 'Download Images'

class ThreadAdmin(admin.ModelAdmin):
    list_display = ['thread_id', 'start_page', 'end_page', 'in_progress', 'is_error']
    actions = [print_images, download_images]

admin.site.register(Thread, ThreadAdmin)
admin.site.register(Image)
