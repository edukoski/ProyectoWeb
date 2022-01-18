from django.contrib import admin
from . models import Categoria, Post

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'updated')

class PostAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'updated')

admin.site.register(Categoria, CategoriaAdmin) # se deben registrar las clases para que aparezcan en el panel de administracion Video 38

admin.site.register(Post, PostAdmin)
