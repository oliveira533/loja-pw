from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:produto_id>', views.produtodesc, name='produtodesc'),
]