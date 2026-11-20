from django.shortcuts import render,get_object_or_404,redirect
from .models import Product

# Create your views here.
def home(request):
  qua = Product.objects.all()
  total = Product.objects.all().count()
  context = {
    'total':total
  }
  return render(request,'base.html',context)

def add(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Product.objects.create(
            product_name=product_name,
            price=price,
            quantity=quantity,
            description=description,
            image=image
        )

        return redirect('product')

    return render(request, 'add.html')

def product(request):
  products = Product.objects.all()
  context= {
    'products':products,
  }
  return render(request,'products.html',context)

def list(request):
  prod = Product.objects.all()
  context = {
    "pro":prod,
  }
  return render(request,'list.html',context)

def details(request,pk):
  detail = get_object_or_404(Product,pk=pk)
  context = {
    'detail':detail,
  }
  return render(request,'details.html',context)

def edit(request,pk):
    det = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        det.product_name = request.POST.get('name')
        det.price = request.POST.get('price')
        det.quantity = request.POST.get('quantity')
        det.description = request.POST.get('description')

        if request.FILES.get('image'):
            det.image = request.FILES.get('image')
        det.save()
        return redirect('product')
    return render(request, 'edit.html', {'det': det})
  
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product')
    return render(request, 'delete.html', {'product': product})