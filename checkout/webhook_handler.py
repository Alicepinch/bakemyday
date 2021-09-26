
from django.http import HttpResponse

class StripeWH_Handler:
    """Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles generic/unknown/unexpected webhook event's
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)