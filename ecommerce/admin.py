from django.contrib import admin
from ecommerce.models import *

class UserPreferenceInLine(admin.TabularInline):
	model = UserPreference
	extra=1

class LoginAccountHistoryInLine(admin.TabularInline):
	model = LoginAccountHistory
	extra=1

class WebContentAssociationInLine(admin.TabularInline):
	model = WebContentAssociation
	extra=1
	fk_name='fromContent'

class WebContentRoleInLine(admin.TabularInline):
	model = WebContentRole
	extra=1

class UserProfileAdmin( admin.ModelAdmin):
	inlines=[ UserPreferenceInLine, LoginAccountHistoryInLine ]

class WebContentAdmin( admin.ModelAdmin):
	inlines=[ WebContentAssociationInLine, WebContentRoleInLine ]

admin.site.register( UserProfile, UserProfileAdmin )
admin.site.register( PreferenceType )
admin.site.register( WebContent, WebContentAdmin )
admin.site.register( FunctionType )
admin.site.register( WebContentRoleType )
admin.site.register( WebContentType )
admin.site.register( WebContentStatusType )

