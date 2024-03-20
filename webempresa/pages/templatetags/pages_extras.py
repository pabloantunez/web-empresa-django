from django import template
from pages.models import Page

register = template.Library() # Reistrar en la libreria de templates.

@register.simple_tag # Decorador que transforma una funcion normal en tag.
def get_page_list():
    pages = Page.objects.all()
    return pages

