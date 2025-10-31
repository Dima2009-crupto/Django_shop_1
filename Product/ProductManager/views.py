from django.shortcuts import render
from django.contrib import messages


from .forms import ProductForm
from .models import Product
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
# Create your views here.



def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            product = form.save(commit=False)
            product = form.save
            messages.success(request, 'Product added successfully!')

    return render(request=request, template_name='add_product.html', context=dict({'form': form}))


def delete_product(request, product_id):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        product.delete()
        messages.success(request, 'Product deleted successfully!')

    return render(request=request, template_name='delete_product.html', context=dict({'product_id': product_id}))


class ProductListView(ListView):
    model = Product
    template_name = 'ProductManager/product_list.html' 
    context_object_name = 'object_list' 
