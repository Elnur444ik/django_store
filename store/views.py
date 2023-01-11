from django.shortcuts import render


def store(request):
    context = {}
    return render(request, 'index.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)


def category(request):
    context = {}
    return render(request, 'store/category.html', context)


def product(request):
    context = {}
    return render(request, 'store/product.html', context)
