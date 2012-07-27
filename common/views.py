from party.models import *
internalOrganizations = Organization.objects.filter( role__role_type__description__exact='Internal Organization')
primaryBusinessFormQuery = internalOrganizations.filter( role__role_type__description__exact='Parent Organization')
organizationRollup = PartyRelationshipType.objects.filter( name__exact='Organization Rollup').get()
departmentRole = PartyRoleType.objects.filter( description__exact='Department').get()
internalOrgRole = PartyRoleType.objects.filter( description__contains='Internal Organization').get()
parentRole = PartyRoleType.objects.filter( description__contains='Parent Organization').get()
customer_role = PartyRoleType.objects.filter( description__exact='Customer').get()

