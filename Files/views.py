from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Files


class IndexView(TemplateView):
    template_name = 'Files/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = Files.objects.all()
        return context

class UploadView(TemplateView):
    template_name = 'Files/upload.html'
