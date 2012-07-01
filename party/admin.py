from party.models import *
from django.contrib import admin


#class PartyClassificationInline(admin.TabularInline):
#	model=PartyClassification
#	extra=1

#class PartyAdmin(admin.ModelAdmin):
#	inlines=[PartyClassificationInline, PartyRoleInLine, PartyContactMechanismInLine ]

admin.site.register(PartyType)
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
