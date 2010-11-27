from common.widgets import DatePickerWidget
from common.forms import CommonModelForm
from products.models import Good


class GoodForm( CommonModelForm ):
	class Meta:
		model=Good
