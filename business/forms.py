from django.forms import DateField, ChoiceField, TextInput
from party.models import Organization, PartyRole, PartyRoleType
from common.widgets import DatePickerWidget
from common.forms import CommonModelForm,make_custom_field

class BusinessForm( CommonModelForm ):
	date_started = DateField(label='Date Started', widget=DatePickerWidget, required=True)
	class Meta:
		model=Organization
		exclude=['roles', 'classification']

class SubOrgForm( BusinessForm ):
	sub_org_role = ChoiceField( label='Organization Type', choices=(
			('Department', 'Department'), 
			('Division', 'Division'),
			('Subsidiary','Subsidiary'),
			('DBA','DBA'))
		)
