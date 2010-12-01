from django.forms import ModelForm
from common.widgets import DatePickerWidget
from common.forms import CommonModelForm
from products.models import Good
from ckeditor.widgets import CKEditorWidget

class GoodForm( CommonModelForm ):
	class Meta:
		model=Good
		widgets = {
			'comment' : CKEditorWidget,
			'introduction_date' : DatePickerWidget,
			'sales_discontinuation_date' : DatePickerWidget,
			'support_discontinuation_date' : DatePickerWidget,
		}

