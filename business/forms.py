from django.forms import DateField, ChoiceField
from party.models import Organization, PartyRole, PartyRoleType
from common.widgets import DatePickerWidget
from common.forms import CommonModelForm

class BusinessForm( CommonModelForm ):
	date_started = DateField(label='Date Started', widget=DatePickerWidget)
	class Meta:
		model=Organization
		fields=['name']

class SubOrgForm( BusinessForm ):
	sub_org_role = ChoiceField( label='Organization Type', choices=(
			('Department', 'Department'), 
			('Division', 'Division'),
			('Subsidiary','Subsidiary'),
			('DBA','DBA'))
		)
