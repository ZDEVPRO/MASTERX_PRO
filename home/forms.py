from django.forms import ModelForm
from .models import Mijozlar_New, Aloqa_New


class QabulForm(ModelForm):
	class Meta:
		model = Mijozlar_New
		fields = '__all__'

class AloqaForm(ModelForm):
	class Meta:
		model = Aloqa_New
		fields = '__all__'

