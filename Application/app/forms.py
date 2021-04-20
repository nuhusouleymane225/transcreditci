from django.forms import ModelForm, fields
from .models import PersonalData, Commentaire, Newsletter

class PersonalDataForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = PersonalData