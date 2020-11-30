from flat.models import Country
from django.forms import ModelForm


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['name', ]
