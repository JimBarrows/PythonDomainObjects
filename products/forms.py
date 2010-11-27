from common.widgets import DatePickerWidget
from common.forms import CommonModelForm
from products.models import Good


class GoodForm( CommonModelForm ):
	class Meta:
		model=Good
		widgets = {
			'introduction_date' : DatePickerWidget,
			'sales_discontinuation_date' : DatePickerWidget,
			'support_discontinuation_date' : DatePickerWidget,
		}
