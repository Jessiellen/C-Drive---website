from django.urls import path, include
from . import views
from .views import IndexView, UploadView

urlpatterns = [
    path('', views.IndexView.as_view(), name='files_index'),
    path('upload/', UploadView.as_view(), name='upload'),
]
