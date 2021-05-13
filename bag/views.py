from django.shortcuts import render, redirect, reverse


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_item(request, item_id):
    """ Adds item to bag in session """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cupcakesize = None
    cakesize = None
    size = None
    if 'cake_size' or 'cupcake_size' in request.POST:
        cakesize = request.POST['cake_size']
        cupcakesize = request.POST['cupcake_size']
        size = cupcakesize or cakesize
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['cakes_by_size'].keys():
                bag[item_id]['cakes_by_size'][size] += quantity
            else:
                bag[item_id]['cakes_by_size'][size] = quantity
        else:
            bag[item_id] = {'cakes_by_size': {size: quantity}}
    else:
    # Increases quantity of product if item is in bag already
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_item(request, item_id):
    """ Adjusts the quantity of item in bag """

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['cakes_by_size'][size] = quantity
        else:
            del bag[item_id]['cakes_by_size'][size]
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            del bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))