from django.forms import ModelForm
from .models import Room
class RoomForm(ModelForm):
    class meta:
        model = Room
        Fields = '__all__'