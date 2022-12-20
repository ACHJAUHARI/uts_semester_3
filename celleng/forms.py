from django.forms import ModelForm
from celleng.models import Ceo

class FormCeo(ModelForm):
    class Meta:
      model = Ceo
      fields =  "__all__"