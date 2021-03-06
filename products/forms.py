from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Occasion


class ProductForm(forms.ModelForm):
    """ Creates product form for product views """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        occasions = Occasion.objects.all()
        cat_friendly_names = [
            (c.id, c.get_friendly_name()) for c in categories]
        occ_friendly_names = [(o.id, o.get_friendly_name()) for o in occasions]

        self.fields['category'].choices = cat_friendly_names
        self.fields['occasion'].choices = occ_friendly_names
