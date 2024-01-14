from django.urls import path
from . import views



app_name = 'shop'

urlpatterns = [

    path('', views.index, name='index'),
    path('product_list', views.product_list, name='product_list'),
    path('contact/', views.contact, name='contact'),
    path('buy/', views.buy, name='buy'),
    path('service/', views.service, name='service'),
    path('gallery/', views.gallery, name='gallery'),
    path('company/', views.company, name='company'),
    path('alimento/', views.alimento, name='alimento'),
    path('agriculture/', views.agriculture, name='agriculture'),
    path('farma/', views.farma, name='farma'),
    path('cosmetico/', views.cosmetico, name='cosmetico'),
    path('textil/', views.textil, name='textil'),
    path('construc/', views.construc, name='construc'),
    path('instrumentos/', views.instrumentos, name='instrumentos'),
    path('repuestos/', views.repuestos, name='repuestos'),
    path('medio_ambiente/', views.medio_ambiente, name='medio_ambiente'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),



]