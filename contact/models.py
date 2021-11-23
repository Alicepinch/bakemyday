from django.db import models


class ContactInquiry(models.Model):
    """ Create contact model in database """

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=320)
    subject = models.CharField(max_length=254, default='Bake My Day Inquiry')
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_on",)

    def __str__(self):
        return self.name