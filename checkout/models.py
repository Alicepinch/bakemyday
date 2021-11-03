import uuid
from django.db.models import Sum
from django.db import models
from django.conf import settings

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """ Creates order in database """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generates unique and permanent,
        random 32 characters order number 
        """

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Generates order total and adds 
        order total to delivery cost 
        """

        self.order_total = self.items.aggregate(Sum('item_total'))['item_total__sum'] or 0
        self.delivery_cost = settings.STANDARD_DELIVERY_PERCENTAGE
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Overrides save method to set order
        number if it hasn't already
        """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    """
    Creates order item in database 
    """

    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(
        max_length=10, null=True, blank=True)  # Cupcake size and cake size
    quantity = models.IntegerField(
        null=False, blank=False, default=0)
    item_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Overrides save method, sets item
        total and updates the order total
        """

        self.item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
