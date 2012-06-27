from django.forms import DateInput

class DatePickerWidget(DateInput):

	def __init__(self):
		attrs={'size':10, 'class': 'datepicker'}
		super(DatePickerWidget, self).__init__(attrs, None )

	class Media:
		css = {
			'all':('css/date_picker.css',)
		}
		js =( 
			'js/date_picker.js',
		)

