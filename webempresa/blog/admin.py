from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # ⇊ Mostrar columnas ⇊
    list_display = ('title', 'author', 'published', 'post_categories' ) #Si se quiere mostrar un atributo que es clave foranea, se debe hacer lo de la linea 26.

    # ⇊ Ordenar por criterios ⇊
    ordering = ('author', 'published') #izq a der. Si es un solo criterio, poner ('xxx',)

    # ⇊ Buscar por atributos ⇊
    search_fields = ('title', 'author__username', 'categories__name') #Si se quiere buscar por una clave foranea, se debe poner el atributo de la tabla. 

    # ⇊ Buscar por fecha ⇊
    date_hierarchy = ('published') #Permite buscar por fechas

    # ⇊ Filtros ⇊
    list_filter = ('author__username', 'categories__name')

    # Se puede acceder al atributo categorias por medio de esta funcion. 
    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')]) #joinea en una lista de categorias que tiene el objeto cada nombre. 
    post_categories.short_description = 'Categorías' # Permite cambiarle el nombre a la columna. 
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
