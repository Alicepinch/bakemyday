from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category, Occasion
from .forms import ProductForm


def all_products(request):
    """ View to return all products, and sorting and searching """

    products = Product.objects.all()
    query = None
    categories = None
    occasions = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'occasion' in request.GET:
            occasions = request.GET['occasion'].split(',')
            products = products.filter(occasion__name__in=occasions)
            occasions = Occasion.objects.filter(name__in=occasions)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter anything!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_occasion': occasions
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product-detail.html', context)


@login_required
def add_product(request):
    """ A view to add a new product to database """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New product succesfully added!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product 😔 Please check form is valid.')
    else:
        form = ProductForm()

    template = 'products/add-product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ A view to delete a product from the database """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f' Succesfully deleted {product.name}')

    return redirect(reverse('products'))


@login_required
def edit_product(request, product_id):
    """ A view to edit an existing product's details in the database """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit-product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)