# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Party'
        db.create_table('party_party', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('party', ['Party'])

        # Adding model 'Person'
        db.create_table('party_person', (
            ('party_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['party.Party'], unique=True, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('party', ['Person'])

        # Adding model 'Organization'
        db.create_table('party_organization', (
            ('party_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['party.Party'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('party', ['Organization'])

        # Adding model 'PartyType'
        db.create_table('party_partytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_set', null=True, to=orm['party.PartyType'])),
        ))
        db.send_create_signal('party', ['PartyType'])

        # Adding model 'PartyClassification'
        db.create_table('party_partyclassification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
            ('party_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PartyType'])),
            ('from_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2010, 12, 8, 21, 5, 11, 758466))),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('party', ['PartyClassification'])

        # Adding model 'PartyRoleType'
        db.create_table('party_partyroletype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_set', null=True, to=orm['party.PartyRoleType'])),
        ))
        db.send_create_signal('party', ['PartyRoleType'])

        # Adding model 'PartyRole'
        db.create_table('party_partyrole', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
            ('party_role_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PartyRoleType'])),
            ('from_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2010, 12, 8, 21, 5, 11, 759952))),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('party', ['PartyRole'])

        # Adding model 'PartyRelationshipType'
        db.create_table('party_partyrelationshiptype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_set', null=True, to=orm['party.PartyRelationshipType'])),
            ('from_role_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_role_type_set', to=orm['party.PartyRoleType'])),
            ('to_role_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_role_type_set', to=orm['party.PartyRoleType'])),
        ))
        db.send_create_signal('party', ['PartyRelationshipType'])

        # Adding model 'PartyRelationship'
        db.create_table('party_partyrelationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('relationship_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PartyRelationshipType'])),
            ('from_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2010, 12, 8, 21, 5, 11, 761858))),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('from_role', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_role_set', to=orm['party.PartyRole'])),
            ('to_role', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_role_set', to=orm['party.PartyRole'])),
            ('priority', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PriorityType'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.StatusType'], null=True, blank=True)),
        ))
        db.send_create_signal('party', ['PartyRelationship'])

        # Adding model 'PartyPostalAddress'
        db.create_table('party_partypostaladdress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('from_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2010, 12, 8, 21, 5, 11, 763665))),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PostalAddress'])),
        ))
        db.send_create_signal('party', ['PartyPostalAddress'])

        # Adding model 'PriorityType'
        db.create_table('party_prioritytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('party', ['PriorityType'])

        # Adding model 'StatusType'
        db.create_table('party_statustype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('party', ['StatusType'])

        # Adding model 'GeographicBoundaryType'
        db.create_table('party_geographicboundarytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('party', ['GeographicBoundaryType'])

        # Adding model 'GeographicBoundary'
        db.create_table('party_geographicboundary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('abbrev', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('geocode', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('geographic_boundary_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.GeographicBoundaryType'])),
        ))
        db.send_create_signal('party', ['GeographicBoundary'])

        # Adding model 'GeographicBoundaryAssociation'
        db.create_table('party_geographicboundaryassociation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contains', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contains_set', to=orm['party.GeographicBoundary'])),
            ('contained_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contained_by_set', to=orm['party.GeographicBoundary'])),
        ))
        db.send_create_signal('party', ['GeographicBoundaryAssociation'])

        # Adding model 'ContactMechanismPurposeType'
        db.create_table('party_contactmechanismpurposetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('party', ['ContactMechanismPurposeType'])

        # Adding model 'ContactMechanism'
        db.create_table('party_contactmechanism', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('party', ['ContactMechanism'])

        # Adding model 'PartyContactMechanism'
        db.create_table('party_partycontactmechanism', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
            ('contact_mechanism', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.ContactMechanism'])),
            ('party_role_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PartyRoleType'], null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('accepts_solicitations', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('party', ['PartyContactMechanism'])

        # Adding model 'PartyContactMechanismPurpose'
        db.create_table('party_partycontactmechanismpurpose', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_mechanism', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PartyContactMechanism'])),
            ('contact_mechanismType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.ContactMechanismPurposeType'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('party', ['PartyContactMechanismPurpose'])

        # Adding model 'PostalAddress'
        db.create_table('party_postaladdress', (
            ('contactmechanism_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['party.ContactMechanism'], unique=True, primary_key=True)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('directions', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('party', ['PostalAddress'])

        # Adding model 'PostalAddressBoundary'
        db.create_table('party_postaladdressboundary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('specified_for', self.gf('django.db.models.fields.related.ForeignKey')(related_name='specified_for', to=orm['party.PostalAddress'])),
            ('in_boundary', self.gf('django.db.models.fields.related.ForeignKey')(related_name='in_boundary', to=orm['party.GeographicBoundary'])),
        ))
        db.send_create_signal('party', ['PostalAddressBoundary'])

        # Adding model 'EmailAddress'
        db.create_table('party_emailaddress', (
            ('contactmechanism_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['party.ContactMechanism'], unique=True, primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('party', ['EmailAddress'])

        # Adding model 'IpAddress'
        db.create_table('party_ipaddress', (
            ('contactmechanism_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['party.ContactMechanism'], unique=True, primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
        ))
        db.send_create_signal('party', ['IpAddress'])

        # Adding model 'WebAddress'
        db.create_table('party_webaddress', (
            ('contactmechanism_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['party.ContactMechanism'], unique=True, primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('party', ['WebAddress'])

        # Adding model 'PhoneNumber'
        db.create_table('party_phonenumber', (
            ('contactmechanism_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['party.ContactMechanism'], unique=True, primary_key=True)),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('area_code', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('extension', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('party', ['PhoneNumber'])

        # Adding model 'FacilityType'
        db.create_table('party_facilitytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('kind_of', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='subType', null=True, to=orm['party.FacilityType'])),
        ))
        db.send_create_signal('party', ['FacilityType'])

        # Adding model 'FacilityRoleType'
        db.create_table('party_facilityroletype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('party', ['FacilityRoleType'])

        # Adding model 'Facility'
        db.create_table('party_facility', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('square_footage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('facility_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.FacilityType'])),
            ('part_of', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='madeUpOf', null=True, to=orm['party.Facility'])),
        ))
        db.send_create_signal('party', ['Facility'])

        # Adding model 'FacilityContactMechanism'
        db.create_table('party_facilitycontactmechanism', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Facility'])),
            ('contact_mechanism', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.ContactMechanism'])),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('accepts_solicitations', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('party', ['FacilityContactMechanism'])

        # Adding model 'FacilityRole'
        db.create_table('party_facilityrole', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'], null=True, blank=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Facility'])),
            ('role_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.FacilityRoleType'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('party', ['FacilityRole'])

        # Adding model 'CommunicationEvent'
        db.create_table('party_communicationevent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_time_started', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_time_ended', self.gf('django.db.models.fields.DateTimeField')()),
            ('note', self.gf('django.db.models.fields.TextField')()),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.CommunicationEventType'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.CommunicationEventStatusType'])),
            ('occurs_via', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.ContactMechanism'])),
            ('context', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PartyRelationship'])),
            ('kase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Kase'])),
        ))
        db.send_create_signal('party', ['CommunicationEvent'])

        # Adding model 'Kase'
        db.create_table('party_kase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_time_started', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('party', ['Kase'])

        # Adding model 'CommunicationEventType'
        db.create_table('party_communicationeventtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('party', ['CommunicationEventType'])

        # Adding model 'CommunicationEventStatusType'
        db.create_table('party_communicationeventstatustype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('party', ['CommunicationEventStatusType'])

        # Adding model 'CommunicationEventRole'
        db.create_table('party_communicationeventrole', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.CommunicationEventRoleType'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.CommunicationEvent'])),
            ('for_a', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('party', ['CommunicationEventRole'])

        # Adding model 'CommunicationEventRoleType'
        db.create_table('party_communicationeventroletype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('party', ['CommunicationEventRoleType'])

        # Adding model 'CommunicationEventPurpose'
        db.create_table('party_communicationeventpurpose', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.CommunicationEventPurposeType'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.CommunicationEvent'])),
            ('for_a', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('party', ['CommunicationEventPurpose'])

        # Adding model 'CommunicationEventPurposeType'
        db.create_table('party_communicationeventpurposetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_set', null=True, to=orm['party.CommunicationEventPurposeType'])),
        ))
        db.send_create_signal('party', ['CommunicationEventPurposeType'])

        # Adding model 'KaseRoleType'
        db.create_table('party_kaseroletype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('party', ['KaseRoleType'])

        # Adding model 'KaseRole'
        db.create_table('party_kaserole', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.KaseRoleType'])),
            ('kase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Kase'])),
            ('for_a', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('party', ['KaseRole'])


    def backwards(self, orm):
        
        # Deleting model 'Party'
        db.delete_table('party_party')

        # Deleting model 'Person'
        db.delete_table('party_person')

        # Deleting model 'Organization'
        db.delete_table('party_organization')

        # Deleting model 'PartyType'
        db.delete_table('party_partytype')

        # Deleting model 'PartyClassification'
        db.delete_table('party_partyclassification')

        # Deleting model 'PartyRoleType'
        db.delete_table('party_partyroletype')

        # Deleting model 'PartyRole'
        db.delete_table('party_partyrole')

        # Deleting model 'PartyRelationshipType'
        db.delete_table('party_partyrelationshiptype')

        # Deleting model 'PartyRelationship'
        db.delete_table('party_partyrelationship')

        # Deleting model 'PartyPostalAddress'
        db.delete_table('party_partypostaladdress')

        # Deleting model 'PriorityType'
        db.delete_table('party_prioritytype')

        # Deleting model 'StatusType'
        db.delete_table('party_statustype')

        # Deleting model 'GeographicBoundaryType'
        db.delete_table('party_geographicboundarytype')

        # Deleting model 'GeographicBoundary'
        db.delete_table('party_geographicboundary')

        # Deleting model 'GeographicBoundaryAssociation'
        db.delete_table('party_geographicboundaryassociation')

        # Deleting model 'ContactMechanismPurposeType'
        db.delete_table('party_contactmechanismpurposetype')

        # Deleting model 'ContactMechanism'
        db.delete_table('party_contactmechanism')

        # Deleting model 'PartyContactMechanism'
        db.delete_table('party_partycontactmechanism')

        # Deleting model 'PartyContactMechanismPurpose'
        db.delete_table('party_partycontactmechanismpurpose')

        # Deleting model 'PostalAddress'
        db.delete_table('party_postaladdress')

        # Deleting model 'PostalAddressBoundary'
        db.delete_table('party_postaladdressboundary')

        # Deleting model 'EmailAddress'
        db.delete_table('party_emailaddress')

        # Deleting model 'IpAddress'
        db.delete_table('party_ipaddress')

        # Deleting model 'WebAddress'
        db.delete_table('party_webaddress')

        # Deleting model 'PhoneNumber'
        db.delete_table('party_phonenumber')

        # Deleting model 'FacilityType'
        db.delete_table('party_facilitytype')

        # Deleting model 'FacilityRoleType'
        db.delete_table('party_facilityroletype')

        # Deleting model 'Facility'
        db.delete_table('party_facility')

        # Deleting model 'FacilityContactMechanism'
        db.delete_table('party_facilitycontactmechanism')

        # Deleting model 'FacilityRole'
        db.delete_table('party_facilityrole')

        # Deleting model 'CommunicationEvent'
        db.delete_table('party_communicationevent')

        # Deleting model 'Kase'
        db.delete_table('party_kase')

        # Deleting model 'CommunicationEventType'
        db.delete_table('party_communicationeventtype')

        # Deleting model 'CommunicationEventStatusType'
        db.delete_table('party_communicationeventstatustype')

        # Deleting model 'CommunicationEventRole'
        db.delete_table('party_communicationeventrole')

        # Deleting model 'CommunicationEventRoleType'
        db.delete_table('party_communicationeventroletype')

        # Deleting model 'CommunicationEventPurpose'
        db.delete_table('party_communicationeventpurpose')

        # Deleting model 'CommunicationEventPurposeType'
        db.delete_table('party_communicationeventpurposetype')

        # Deleting model 'KaseRoleType'
        db.delete_table('party_kaseroletype')

        # Deleting model 'KaseRole'
        db.delete_table('party_kaserole')


    models = {
        'party.communicationevent': {
            'Meta': {'object_name': 'CommunicationEvent'},
            'categorized_by': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['party.CommunicationEventPurposeType']", 'through': "orm['party.CommunicationEventPurpose']", 'symmetrical': 'False'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyRelationship']"}),
            'date_time_ended': ('django.db.models.fields.DateTimeField', [], {}),
            'date_time_started': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'involving': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['party.CommunicationEventRoleType']", 'through': "orm['party.CommunicationEventRole']", 'symmetrical': 'False'}),
            'kase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Kase']"}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.CommunicationEventType']"}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'occurs_via': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.ContactMechanism']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.CommunicationEventStatusType']"})
        },
        'party.communicationeventpurpose': {
            'Meta': {'object_name': 'CommunicationEventPurpose'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.CommunicationEvent']"}),
            'for_a': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.CommunicationEventPurposeType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.communicationeventpurposetype': {
            'Meta': {'object_name': 'CommunicationEventPurposeType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['party.CommunicationEventPurposeType']"})
        },
        'party.communicationeventrole': {
            'Meta': {'object_name': 'CommunicationEventRole'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.CommunicationEvent']"}),
            'for_a': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.CommunicationEventRoleType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.communicationeventroletype': {
            'Meta': {'object_name': 'CommunicationEventRoleType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'party.communicationeventstatustype': {
            'Meta': {'object_name': 'CommunicationEventStatusType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'party.communicationeventtype': {
            'Meta': {'object_name': 'CommunicationEventType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'party.contactmechanism': {
            'Meta': {'object_name': 'ContactMechanism'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'party.contactmechanismpurposetype': {
            'Meta': {'object_name': 'ContactMechanismPurposeType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'party.emailaddress': {
            'Meta': {'object_name': 'EmailAddress', '_ormbases': ['party.ContactMechanism']},
            'contactmechanism_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['party.ContactMechanism']", 'unique': 'True', 'primary_key': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'})
        },
        'party.facility': {
            'Meta': {'object_name': 'Facility'},
            'contact_mechanisms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['party.ContactMechanism']", 'through': "orm['party.FacilityContactMechanism']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'facility_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.FacilityType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'madeUpOf'", 'null': 'True', 'to': "orm['party.Facility']"}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['party.FacilityRoleType']", 'through': "orm['party.FacilityRole']", 'symmetrical': 'False'}),
            'square_footage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.facilitycontactmechanism': {
            'Meta': {'object_name': 'FacilityContactMechanism'},
            'accepts_solicitations': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_mechanism': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.ContactMechanism']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Facility']"}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.facilityrole': {
            'Meta': {'object_name': 'FacilityRole'},
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Facility']"}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']", 'null': 'True', 'blank': 'True'}),
            'role_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.FacilityRoleType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.facilityroletype': {
            'Meta': {'object_name': 'FacilityRoleType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'party.facilitytype': {
            'Meta': {'object_name': 'FacilityType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'subType'", 'null': 'True', 'to': "orm['party.FacilityType']"})
        },
        'party.geographicboundary': {
            'Meta': {'object_name': 'GeographicBoundary'},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'geocode': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'geographic_boundary_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.GeographicBoundaryType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        'party.geographicboundaryassociation': {
            'Meta': {'object_name': 'GeographicBoundaryAssociation'},
            'contained_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contained_by_set'", 'to': "orm['party.GeographicBoundary']"}),
            'contains': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contains_set'", 'to': "orm['party.GeographicBoundary']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'party.geographicboundarytype': {
            'Meta': {'object_name': 'GeographicBoundaryType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'party.ipaddress': {
            'Meta': {'object_name': 'IpAddress', '_ormbases': ['party.ContactMechanism']},
            'contactmechanism_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['party.ContactMechanism']", 'unique': 'True', 'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'})
        },
        'party.kase': {
            'Meta': {'object_name': 'Kase'},
            'date_time_started': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'involving': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['party.KaseRoleType']", 'through': "orm['party.KaseRole']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'party.kaserole': {
            'Meta': {'object_name': 'KaseRole'},
            'for_a': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Kase']"}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.KaseRoleType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.kaseroletype': {
            'Meta': {'object_name': 'KaseRoleType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'party.organization': {
            'Meta': {'object_name': 'Organization', '_ormbases': ['party.Party']},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'party_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['party.Party']", 'unique': 'True', 'primary_key': 'True'})
        },
        'party.party': {
            'Meta': {'object_name': 'Party'},
            'classification': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['party.PartyType']", 'through': "orm['party.PartyClassification']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['party.PartyRoleType']", 'through': "orm['party.PartyRole']", 'symmetrical': 'False'})
        },
        'party.partyclassification': {
            'Meta': {'object_name': 'PartyClassification'},
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 5, 11, 758466)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'party_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.partycontactmechanism': {
            'Meta': {'object_name': 'PartyContactMechanism'},
            'accepts_solicitations': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_mechanism': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.ContactMechanism']"}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'party_role_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyRoleType']", 'null': 'True', 'blank': 'True'}),
            'purpose': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['party.ContactMechanismPurposeType']", 'through': "orm['party.PartyContactMechanismPurpose']", 'symmetrical': 'False'}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.partycontactmechanismpurpose': {
            'Meta': {'object_name': 'PartyContactMechanismPurpose'},
            'contact_mechanism': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyContactMechanism']"}),
            'contact_mechanismType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.ContactMechanismPurposeType']"}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.partypostaladdress': {
            'Meta': {'object_name': 'PartyPostalAddress'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 5, 11, 763665)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PostalAddress']"}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.partyrelationship': {
            'Meta': {'object_name': 'PartyRelationship'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 5, 11, 761858)'}),
            'from_role': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_role_set'", 'to': "orm['party.PartyRole']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PriorityType']", 'null': 'True', 'blank': 'True'}),
            'relationship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyRelationshipType']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.StatusType']", 'null': 'True', 'blank': 'True'}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'to_role': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_role_set'", 'to': "orm['party.PartyRole']"})
        },
        'party.partyrelationshiptype': {
            'Meta': {'object_name': 'PartyRelationshipType'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'from_role_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_role_type_set'", 'to': "orm['party.PartyRoleType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['party.PartyRelationshipType']"}),
            'to_role_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_role_type_set'", 'to': "orm['party.PartyRoleType']"})
        },
        'party.partyrole': {
            'Meta': {'object_name': 'PartyRole'},
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 5, 11, 759952)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'party_role_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyRoleType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.partyroletype': {
            'Meta': {'ordering': "['description']", 'object_name': 'PartyRoleType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['party.PartyRoleType']"})
        },
        'party.partytype': {
            'Meta': {'object_name': 'PartyType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['party.PartyType']"})
        },
        'party.person': {
            'Meta': {'object_name': 'Person', '_ormbases': ['party.Party']},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'party_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['party.Party']", 'unique': 'True', 'primary_key': 'True'})
        },
        'party.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber', '_ormbases': ['party.ContactMechanism']},
            'area_code': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'contactmechanism_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['party.ContactMechanism']", 'unique': 'True', 'primary_key': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'party.postaladdress': {
            'Meta': {'object_name': 'PostalAddress', '_ormbases': ['party.ContactMechanism']},
            'contactmechanism_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['party.ContactMechanism']", 'unique': 'True', 'primary_key': 'True'}),
            'directions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        'party.postaladdressboundary': {
            'Meta': {'object_name': 'PostalAddressBoundary'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_boundary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_boundary'", 'to': "orm['party.GeographicBoundary']"}),
            'specified_for': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'specified_for'", 'to': "orm['party.PostalAddress']"})
        },
        'party.prioritytype': {
            'Meta': {'object_name': 'PriorityType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'party.statustype': {
            'Meta': {'object_name': 'StatusType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'party.webaddress': {
            'Meta': {'object_name': 'WebAddress', '_ormbases': ['party.ContactMechanism']},
            'contactmechanism_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['party.ContactMechanism']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['party']
