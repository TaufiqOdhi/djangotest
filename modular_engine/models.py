from django.db import models

# Create your models here.
class AppModule(models.Model):
    name = models.CharField(max_length=225)
    is_installed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
