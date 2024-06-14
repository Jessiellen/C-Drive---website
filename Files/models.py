# from django.core.validators import FileSizeValidator
from django.db import models
from django.conf import settings

class Category(models.Model):
    nome = models.CharField(max_length=100)
    id = models.BigAutoField(primary_key=True)
    
    def __str__(self): 
        return self.nome
    
    class Meta:  
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = ['id']

class Files(models.Model):
    title = models.CharField(max_length=200)
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.title
