from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView

from .forms import ProductForm, SignUp, LogIn
from .models import Product

# Create your views here.


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



def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = SignUp(data = request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        messages.success(request, 'Аккаунт створино.')
        return redirect('login')
    return render(request=request, template_name='registration/sign_up.html', context={'form': form})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = LogIn(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
            user = autheficate(
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password"),
            )
            if user:
                login(request=request, user=user)
                messages.add_message(request=request, level=messages.SUCCESS, message="Успішний вхід!")
                return redirect("index")
            else:
                messages.add_message(request=request, level=messages.ERROR, message="Невірний логін або пароль.")
    return render(request=request, template_name="registration/sign_in.html", context={"form": form})


@login_required(login_url="/sign_in/")
def index(request):
    return render(request=request, template_name="index.html")



























def cookie_consent(request):
    if request.method == 'POST':
        resp = redirect('home')
        resp.set_cookie('cookie_consent', 'accepted', max_age=365*24*60*60)
        return resp
    consent = request.COOKIES.get('cookie_consent')
    return render(request, 'cookie_consent.html', {'consent': consent})