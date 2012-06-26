from django.forms import DateInput

class DatePickerWidget(DateInput):

    def __init__(self, **kwargs):
        super(DateInput, self).__init__(attrs={'size':10, 'class': 'datepicker'}, **kwargs)

    class Media:
        css = {
        	'all':('css/date_picker.css',)
        }
        js =( 
        	'js/date_picker.js',
        	)

