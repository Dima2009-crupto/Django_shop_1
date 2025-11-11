from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.http import HttpResponse
from .forms import ProductForm, SignUpForm
from .models import Product




def home(request):
    return render(request, 'home.html')



class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 6


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

def login_view(request):
    if request.method == 'POST':
        form = authenticate (request, data=request.POST)
        if form.is_valid():
            from django.contrib.auth import login as auth_login
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
        
    else:
        form = authenticate()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт створино.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



def cookie_consent(request):
    if request.method == 'POST':
        resp = redirect('home')
        resp.set_cookie('cookie_consent', 'accepted', max_age=365*24*60*60)
        return resp
    consent = request.COOKIES.get('cookie_consent')
    return render(request, 'cookie_consent.html', {'consent': consent})