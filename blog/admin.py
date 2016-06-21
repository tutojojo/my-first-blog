from django.contrib import admin
# Register your models here.
from .models import Post
admin.site.register(Post) # Afin que notre modèle soit visible dans l'interface d'administration
