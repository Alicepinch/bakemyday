from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    delivery = total + settings.STANDARD_DELIVERY_PERCENTAGE

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
    }

    return context
