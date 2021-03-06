from party.models import *
from django.contrib import admin


class IdentifierInline(admin.TabularInline):
	model=Identifier
	extra=1

class PartyClassificationInline(admin.TabularInline):
	model=PartyClassification
	extra=1

class PartyRoleInLine(admin.TabularInline):
	model=PartyRole
	extra=1

class PartyContactMechanismInLine(admin.TabularInline):
	model=PartyContactMechanism
	extra=1

class PartyAdmin(admin.ModelAdmin):
	inlines=[IdentifierInline, PartyClassificationInline, PartyRoleInLine, PartyContactMechanismInLine ]

admin.site.register(Person, PartyAdmin)
admin.site.register(Organization, PartyAdmin)
admin.site.register(PartyType)
admin.site.register(PartyRoleType)
admin.site.register(OrganizationType)
admin.site.register(MinorityClassificationType)
admin.site.register(IndustryClassificationType)
admin.site.register(SizeClassificationType)
admin.site.register(PersonType)
admin.site.register(EeocClassificationType)
admin.site.register(IncomeClassificationType)

admin.site.register(PartyClassification)
admin.site.register(OrganizationClassification)
admin.site.register(MinorityClassification)
admin.site.register(IndustryClassification)
admin.site.register(SizeClassification)
admin.site.register(PersonClassification)
admin.site.register(EeocClassification)
admin.site.register(IncomeClassification)
admin.site.register(IdentificationType)
