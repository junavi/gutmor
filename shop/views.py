from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .forms import EmailContactForm




def index(request):
    return render(request, 'shop/index.html')


def contact(request):
    data = {
        'form': EmailContactForm()
    }
    if request.method == 'POST':
        formulario = EmailContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Gracias por contactarnos!!!"
        else:
            data["form"] = formulario

    return render(request, 'shop/contact.html',data)

def popular(request):
    return render(request, 'shop/popular.html')

def default(request):
    return render(request, 'shop/default.html')

def alimento(request):
    categories = Category.objects.order_by()
    products = Product.objects.filter(available=True)

    return render(request,
                  'shop/alimento.html',
                  {'categories': categories,
                  'products': products})
def agriculture(request):
    categories = Category.objects.order_by()
    products = Product.objects.filter(available=True)

    return render(request,
                  'shop/agricultura.html',
                  {'categories': categories,
                  'products': products})
def farma(request):
    categories = Category.objects.order_by()
    products = Product.objects.filter(available=True)

    return render(request,
                  'shop/farmacia.html',
                  {'categories': categories,
                  'products': products})
def cosmetico(request):
    categories = Category.objects.order_by()
    products = Product.objects.filter(available=True)

    return render(request,
                  'shop/cosmetico.html',
                  {'categories': categories,
                  'products': products})
def construc(request):
    categories = Category.objects.order_by()
    products = Product.objects.filter(available=True)

    return render(request,
                  'shop/construccion.html',
                  {'categories': categories,
                  'products': products})
def textil(request):
    categories = Category.objects.order_by()
    products = Product.objects.filter(available=True)

    return render(request,
                  'shop/textil.html',
                  {'categories': categories,
                  'products': products})

def instrumentos(request):
    categories = Category.objects.order_by()
    products = Product.objects.filter(available=True)

    return render(request,
                  'shop/instrumentos.html',
                  {'categories': categories,
                   'products': products})
def repuestos(request):
    categories = Category.objects.order_by()
    products = Product.objects.filter(available=True)

    return render(request,
                  'shop/repuestos.html',
                  {'categories': categories,
                   'products': products})
def medio_ambiente(request):
    categories = Category.objects.order_by()
    products = Product.objects.filter(available=True)

    return render(request,
                  'shop/medio-ambiente.html',
                  {'categories': categories,
                   'products': products})
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})