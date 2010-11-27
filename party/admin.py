from party.models import *
from django.contrib import admin


class PartyClassificationInline(admin.TabularInline):
	model=PartyClassification
	extra=1

class PartyRoleInLine(admin.TabularInline):
	model=PartyRole
	extra=1

class PartyRoleTypeInLine(admin.TabularInline):
	model=PartyRoleType
	extra=1

class PartyTypeInLine(admin.TabularInline):
	model=PartyType
	extra=1

class CommunicationEventInLine(admin.TabularInline):
	model=CommunicationEvent
	extra=1

class PartyRelationshipTypeInLine(admin.TabularInline):
	model=PartyRelationshipType
	extra=1

class ContainsGeographicBoundaryAssociationInLine(admin.TabularInline):
	model=GeographicBoundaryAssociation
	fk_name='contains'
	extra=1

class ContainedByGeographicBoundaryAssociationInLine(admin.TabularInline):
	model=GeographicBoundaryAssociation
	fk_name='contained_by'

class ContainedByGeographicBoundaryAssociationInLine(admin.TabularInline):
	model=GeographicBoundaryAssociation
	fk_name='contained_by'

class SpecifiedForPostalAddressBoundaryInLine(admin.TabularInline):
	model=PostalAddressBoundary
	fk_name='specified_for'

class InBoundaryPostalAddressBoundaryInLine(admin.TabularInline):
	model=PostalAddressBoundary
	fk_name='in_boundary'

class PartyPostalAddressInLine(admin.TabularInline):
	model=PartyPostalAddress
	extra=1

class PartyContactMechanismInLine(admin.TabularInline):
	model=PartyContactMechanism
	extra=1

class PartyContactMechanismPurposeInLine(admin.TabularInline):
	model=PartyContactMechanismPurpose
	extra=1

class FacilityInLine(admin.TabularInline):
	model=Facility
	extra=1

class FacilityRoleInLine(admin.TabularInline):
	model=FacilityRole
	extra=1

class FacilityTypeInLine(admin.TabularInline):
	model=FacilityType
	extra=1

class FacilityContactMechanismInLine(admin.TabularInline):
	model=FacilityContactMechanism
	extra=1

class CommunicationEventPurposeInLine(admin.TabularInline):
	model=CommunicationEventPurpose
	extra=1

class CommunicationEventRoleInLine(admin.TabularInline):
	model=CommunicationEventRole
	extra=1

class KaseRoleInLine(admin.TabularInline):
	model=KaseRole
	extra=1

class PartyAdmin(admin.ModelAdmin):
	inlines=[PartyClassificationInline, PartyRoleInLine, PartyContactMechanismInLine ]

class PartyRoleTypeAdmin(admin.ModelAdmin):
	inlines=[ PartyRoleTypeInLine]

class PartyTypeAdmin(admin.ModelAdmin):
	inlines=[ PartyTypeInLine]

class PartyRelationshipTypeAdmin(admin.ModelAdmin):
	inlines=[ PartyRelationshipTypeInLine]

class PartyRelationshipAdmin(admin.ModelAdmin):
	inlines=[ CommunicationEventInLine]

class GeographicBoundaryAdmin(admin.ModelAdmin):
	inlines=[ ContainsGeographicBoundaryAssociationInLine, 
		ContainedByGeographicBoundaryAssociationInLine
	]

class PostalAddressAdmin(admin.ModelAdmin):
	inlines=[ SpecifiedForPostalAddressBoundaryInLine
	]

class PartyRelationshipAdmin(admin.ModelAdmin):
	inlines=[ CommunicationEventInLine]

class PartyContactMechanismAdmin(admin.ModelAdmin):
	inlines=[ PartyContactMechanismPurposeInLine]

class FacilityAdmin(admin.ModelAdmin):
	inlines=[ FacilityInLine, FacilityRoleInLine, FacilityContactMechanismInLine]

class FacilityTypeAdmin(admin.ModelAdmin):
	inlines=[ FacilityTypeInLine]

class CommunicationEventAdmin(admin.ModelAdmin):
	inlines=[ CommunicationEventPurposeInLine,CommunicationEventRoleInLine]

class KaseAdmin(admin.ModelAdmin):
	inlines=[ KaseRoleInLine]

admin.site.register(Person, PartyAdmin)
admin.site.register(Organization, PartyAdmin)
admin.site.register(PartyType, PartyTypeAdmin)
admin.site.register(PartyRoleType, PartyRoleTypeAdmin)
admin.site.register(PartyRelationshipType, PartyRelationshipTypeAdmin)
admin.site.register(PartyRelationship, PartyRelationshipAdmin )
admin.site.register(PriorityType )
admin.site.register(StatusType )
admin.site.register(GeographicBoundaryType )
admin.site.register(GeographicBoundary, GeographicBoundaryAdmin )
admin.site.register(GeographicBoundaryAssociation)
admin.site.register(PostalAddress, PostalAddressAdmin)
admin.site.register(PostalAddressBoundary)
admin.site.register(ContactMechanismPurposeType )
admin.site.register(PartyContactMechanism, PartyContactMechanismAdmin )
admin.site.register(EmailAddress )
admin.site.register(IpAddress )
admin.site.register(WebAddress )
admin.site.register(PhoneNumber )
admin.site.register(FacilityType, FacilityTypeAdmin )
admin.site.register(FacilityRoleType )
admin.site.register(Facility, FacilityAdmin )
admin.site.register(CommunicationEventType )
admin.site.register(CommunicationEventStatusType )
admin.site.register(CommunicationEventPurposeType )
admin.site.register(CommunicationEvent, CommunicationEventAdmin)
admin.site.register(KaseRoleType )
admin.site.register(Kase, KaseAdmin )
