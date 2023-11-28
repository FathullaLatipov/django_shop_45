from django.contrib.auth import logout
from django.shortcuts import render, redirect

from products.models import ProductModel, CategoryModel

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


def home_page(request):
    products = ProductModel.objects.all()
    categories = CategoryModel.objects.all()

    context = {'products': products, 'categories': categories}
    return render(request, 'index.html', context)


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home_page')


def logout_view(request):
    logout(request)
    return redirect('home_page')


def single_product(request, pk):
    product = ProductModel.objects.get(pk=pk)


    context = {'product': product}
    return render(request, 'single-products.html', context)
