from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_item(request, item_id):
    """ A view to add items to bag in session """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cupcakesize = None
    cakesize = None
    size = None
    if 'cake_size' or 'cupcake_size' in request.POST:
        cakesize = request.POST.get('cake_size', False)
        cupcakesize = request.POST.get('cupcake_size', False)
        size = cupcakesize or cakesize

    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['cakes_by_size'].keys():
                bag[item_id]['cakes_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Added another {size}{product.name} to bag, quantity \
                    is now {bag[item_id]["cakes_by_size"][size]}')
            else:
                bag[item_id]['cakes_by_size'][size] = quantity
                messages.success(
                    request, f'Added {size} {product.name} to bag')
        else:
            bag[item_id] = {'cakes_by_size': {size: quantity}}
            messages.success(request, f'Added {size} {product.name} to bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_item(request, item_id):
    """ A view to adjusts the quantity of items within bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['cakes_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated {product.name} {size} quantity \
                to {bag[item_id] ["cakes_by_size"][size]}')
        else:
            del bag[item_id]['cakes_by_size'][size]
            if not bag[item_id]['cakes_by_size']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed {size} {product.name} from bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_item(request, item_id):
    """ A view to remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['cakes_by_size'][size]
            if not bag[item_id]['cakes_by_size']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed {size} {product.name} from bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
