from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name='category') # El <category_id> es un campo variable. No estatico. Es siempre es un string, el 'int:' cambia el tipo de dato del category_id.

]