# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UserProfile'
        db.create_table('ecommerce_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
            ('web_address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.WebAddress'])),
        ))
        db.send_create_signal('ecommerce', ['UserProfile'])

        # Adding model 'LoginAccountHistory'
        db.create_table('ecommerce_loginaccounthistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecommerce.UserProfile'])),
        ))
        db.send_create_signal('ecommerce', ['LoginAccountHistory'])

        # Adding model 'PreferenceType'
        db.create_table('ecommerce_preferencetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('ecommerce', ['PreferenceType'])

        # Adding model 'UserPreference'
        db.create_table('ecommerce_userpreference', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecommerce.UserProfile'])),
            ('preference_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecommerce.PreferenceType'])),
        ))
        db.send_create_signal('ecommerce', ['UserPreference'])

        # Adding model 'WebContent'
        db.create_table('ecommerce_webcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecommerce.WebContentType'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecommerce.WebContentStatusType'])),
            ('web_address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.WebAddress'])),
        ))
        db.send_create_signal('ecommerce', ['WebContent'])

        # Adding model 'WebContentRoleType'
        db.create_table('ecommerce_webcontentroletype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('ecommerce', ['WebContentRoleType'])

        # Adding model 'WebContentStatusType'
        db.create_table('ecommerce_webcontentstatustype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('ecommerce', ['WebContentStatusType'])

        # Adding model 'WebContentType'
        db.create_table('ecommerce_webcontenttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('ecommerce', ['WebContentType'])

        # Adding model 'WebContentRole'
        db.create_table('ecommerce_webcontentrole', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecommerce.WebContent'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecommerce.WebContentRoleType'])),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('ecommerce', ['WebContentRole'])

        # Adding model 'WebContentAssociation'
        db.create_table('ecommerce_webcontentassociation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
            ('from_content', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_content_set', to=orm['ecommerce.WebContent'])),
            ('to_content', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_content_set', to=orm['ecommerce.WebContent'])),
            ('function', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecommerce.FunctionType'])),
        ))
        db.send_create_signal('ecommerce', ['WebContentAssociation'])

        # Adding model 'FunctionType'
        db.create_table('ecommerce_functiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('ecommerce', ['FunctionType'])

        # Adding model 'WebObject'
        db.create_table('ecommerce_webobject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecommerce.WebObjectType'])),
        ))
        db.send_create_signal('ecommerce', ['WebObject'])

        # Adding M2M table for field features on 'WebObject'
        db.create_table('ecommerce_webobject_features', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('webobject', models.ForeignKey(orm['ecommerce.webobject'], null=False)),
            ('feature', models.ForeignKey(orm['products.feature'], null=False))
        ))
        db.create_unique('ecommerce_webobject_features', ['webobject_id', 'feature_id'])

        # Adding M2M table for field purposes on 'WebObject'
        db.create_table('ecommerce_webobject_purposes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('webobject', models.ForeignKey(orm['ecommerce.webobject'], null=False)),
            ('purposetype', models.ForeignKey(orm['ecommerce.purposetype'], null=False))
        ))
        db.create_unique('ecommerce_webobject_purposes', ['webobject_id', 'purposetype_id'])

        # Adding M2M table for field products on 'WebObject'
        db.create_table('ecommerce_webobject_products', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('webobject', models.ForeignKey(orm['ecommerce.webobject'], null=False)),
            ('product', models.ForeignKey(orm['products.product'], null=False))
        ))
        db.create_unique('ecommerce_webobject_products', ['webobject_id', 'product_id'])

        # Adding model 'WebObjectType'
        db.create_table('ecommerce_webobjecttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('ecommerce', ['WebObjectType'])

        # Adding model 'ObjectUsage'
        db.create_table('ecommerce_objectusage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('web_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecommerce.WebObject'])),
            ('web_content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecommerce.WebContent'])),
        ))
        db.send_create_signal('ecommerce', ['ObjectUsage'])

        # Adding model 'PurposeType'
        db.create_table('ecommerce_purposetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('ecommerce', ['PurposeType'])

        # Adding model 'Subscription'
        db.create_table('ecommerce_subscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')()),
            ('orderItem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.OrderItem'])),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecommerce.SubscriptionType'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
            ('subscriber', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PartyRole'])),
            ('sent_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.ContactMechanism'])),
            ('originating_from', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.CommunicationEvent'])),
        ))
        db.send_create_signal('ecommerce', ['Subscription'])

        # Adding M2M table for field fullfilled_via on 'Subscription'
        db.create_table('ecommerce_subscription_fullfilled_via', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subscription', models.ForeignKey(orm['ecommerce.subscription'], null=False)),
            ('subscriptionactivity', models.ForeignKey(orm['ecommerce.subscriptionactivity'], null=False))
        ))
        db.create_unique('ecommerce_subscription_fullfilled_via', ['subscription_id', 'subscriptionactivity_id'])

        # Adding model 'SubscriptionActivity'
        db.create_table('ecommerce_subscriptionactivity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_sent', self.gf('django.db.models.fields.DateField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('ecommerce', ['SubscriptionActivity'])

        # Adding model 'SubscriptionType'
        db.create_table('ecommerce_subscriptiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('ecommerce', ['SubscriptionType'])


    def backwards(self, orm):
        
        # Deleting model 'UserProfile'
        db.delete_table('ecommerce_userprofile')

        # Deleting model 'LoginAccountHistory'
        db.delete_table('ecommerce_loginaccounthistory')

        # Deleting model 'PreferenceType'
        db.delete_table('ecommerce_preferencetype')

        # Deleting model 'UserPreference'
        db.delete_table('ecommerce_userpreference')

        # Deleting model 'WebContent'
        db.delete_table('ecommerce_webcontent')

        # Deleting model 'WebContentRoleType'
        db.delete_table('ecommerce_webcontentroletype')

        # Deleting model 'WebContentStatusType'
        db.delete_table('ecommerce_webcontentstatustype')

        # Deleting model 'WebContentType'
        db.delete_table('ecommerce_webcontenttype')

        # Deleting model 'WebContentRole'
        db.delete_table('ecommerce_webcontentrole')

        # Deleting model 'WebContentAssociation'
        db.delete_table('ecommerce_webcontentassociation')

        # Deleting model 'FunctionType'
        db.delete_table('ecommerce_functiontype')

        # Deleting model 'WebObject'
        db.delete_table('ecommerce_webobject')

        # Removing M2M table for field features on 'WebObject'
        db.delete_table('ecommerce_webobject_features')

        # Removing M2M table for field purposes on 'WebObject'
        db.delete_table('ecommerce_webobject_purposes')

        # Removing M2M table for field products on 'WebObject'
        db.delete_table('ecommerce_webobject_products')

        # Deleting model 'WebObjectType'
        db.delete_table('ecommerce_webobjecttype')

        # Deleting model 'ObjectUsage'
        db.delete_table('ecommerce_objectusage')

        # Deleting model 'PurposeType'
        db.delete_table('ecommerce_purposetype')

        # Deleting model 'Subscription'
        db.delete_table('ecommerce_subscription')

        # Removing M2M table for field fullfilled_via on 'Subscription'
        db.delete_table('ecommerce_subscription_fullfilled_via')

        # Deleting model 'SubscriptionActivity'
        db.delete_table('ecommerce_subscriptionactivity')

        # Deleting model 'SubscriptionType'
        db.delete_table('ecommerce_subscriptiontype')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ecommerce.functiontype': {
            'Meta': {'object_name': 'FunctionType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ecommerce.loginaccounthistory': {
            'Meta': {'object_name': 'LoginAccountHistory'},
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ecommerce.UserProfile']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'ecommerce.objectusage': {
            'Meta': {'object_name': 'ObjectUsage'},
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'web_content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ecommerce.WebContent']"}),
            'web_object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ecommerce.WebObject']"})
        },
        'ecommerce.preferencetype': {
            'Meta': {'object_name': 'PreferenceType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ecommerce.purposetype': {
            'Meta': {'object_name': 'PurposeType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ecommerce.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'end': ('django.db.models.fields.DateField', [], {}),
            'fullfilled_via': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ecommerce.SubscriptionActivity']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ecommerce.SubscriptionType']"}),
            'orderItem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.OrderItem']"}),
            'originating_from': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.CommunicationEvent']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'sent_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.ContactMechanism']"}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'subscriber': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyRole']"})
        },
        'ecommerce.subscriptionactivity': {
            'Meta': {'object_name': 'SubscriptionActivity'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date_sent': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ecommerce.subscriptiontype': {
            'Meta': {'object_name': 'SubscriptionType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ecommerce.userpreference': {
            'Meta': {'object_name': 'UserPreference'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preference_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ecommerce.PreferenceType']"}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ecommerce.UserProfile']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'ecommerce.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'preferences': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ecommerce.PreferenceType']", 'through': "orm['ecommerce.UserPreference']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'web_address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.WebAddress']"})
        },
        'ecommerce.webcontent': {
            'Meta': {'object_name': 'WebContent'},
            'associated': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['ecommerce.WebContent']", 'null': 'True', 'through': "orm['ecommerce.WebContentAssociation']", 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ecommerce.WebContentType']"}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['ecommerce.WebContentRoleType']", 'null': 'True', 'through': "orm['ecommerce.WebContentRole']", 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ecommerce.WebContentStatusType']"}),
            'web_address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.WebAddress']"})
        },
        'ecommerce.webcontentassociation': {
            'Meta': {'object_name': 'WebContentAssociation'},
            'from_content': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_content_set'", 'to': "orm['ecommerce.WebContent']"}),
            'function': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ecommerce.FunctionType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_content': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_content_set'", 'to': "orm['ecommerce.WebContent']"}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        },
        'ecommerce.webcontentrole': {
            'Meta': {'object_name': 'WebContentRole'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ecommerce.WebContent']"}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ecommerce.WebContentRoleType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'ecommerce.webcontentroletype': {
            'Meta': {'object_name': 'WebContentRoleType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ecommerce.webcontentstatustype': {
            'Meta': {'object_name': 'WebContentStatusType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ecommerce.webcontenttype': {
            'Meta': {'object_name': 'WebContentType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ecommerce.webobject': {
            'Meta': {'object_name': 'WebObject'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Feature']", 'symmetrical': 'False'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ecommerce.WebObjectType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['products.Product']", 'null': 'True', 'blank': 'True'}),
            'purposes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['ecommerce.PurposeType']", 'null': 'True', 'blank': 'True'}),
            'usage': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ecommerce.WebContent']", 'through': "orm['ecommerce.ObjectUsage']", 'symmetrical': 'False'})
        },
        'ecommerce.webobjecttype': {
            'Meta': {'object_name': 'WebObjectType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'orders.orderitem': {
            'Meta': {'object_name': 'OrderItem'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'estimated_delivery_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_description': ('django.db.models.fields.TextField', [], {}),
            'ordered_with': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['orders.OrderItem']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'product_feature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Feature']"}),
            'shipping_instructions': ('django.db.models.fields.TextField', [], {}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 5, 40, 466719)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'party_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.partyrelationship': {
            'Meta': {'object_name': 'PartyRelationship'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 5, 40, 469928)'}),
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 5, 40, 468196)'}),
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
        },
        'products.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'of_interest_to': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['party.PartyType']", 'through': "orm['products.MarketInterest']", 'symmetrical': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['products.Category']"})
        },
        'products.categoryclassification': {
            'Meta': {'object_name': 'CategoryClassification'},
            'category_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 5, 40, 563427)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'products.feature': {
            'Meta': {'object_name': 'Feature'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.FeatureCategory']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_products.feature_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'product': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['products.Product']", 'through': "orm['products.FeatureApplicability']", 'symmetrical': 'False'})
        },
        'products.featureapplicability': {
            'Meta': {'object_name': 'FeatureApplicability'},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Feature']"}),
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 5, 40, 572769)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'products.featurecategory': {
            'Meta': {'object_name': 'FeatureCategory'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.marketinterest': {
            'Meta': {'object_name': 'MarketInterest'},
            'category_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 5, 40, 576083)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'products.part': {
            'Meta': {'object_name': 'Part'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_products.part_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"})
        },
        'products.preferencetype': {
            'Meta': {'object_name': 'PreferenceType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.product': {
            'Meta': {'ordering': "['name']", 'object_name': 'Product'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['products.Category']", 'null': 'True', 'through': "orm['products.CategoryClassification']", 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'manufactured_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'producerOf_set'", 'null': 'True', 'to': "orm['party.Organization']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_products.product_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'sales_discontinuation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'suppliers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['party.Organization']", 'null': 'True', 'through': "orm['products.SupplierProduct']", 'blank': 'True'}),
            'support_discontinuation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'products.ratingtype': {
            'Meta': {'object_name': 'RatingType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.supplierproduct': {
            'Meta': {'object_name': 'SupplierProduct'},
            'available_from': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 5, 40, 559794)'}),
            'available_thru': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Organization']"}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Part']", 'null': 'True', 'blank': 'True'}),
            'preference': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.PreferenceType']", 'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'rating': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.RatingType']", 'null': 'True', 'blank': 'True'}),
            'standard_lead_time_in_days': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ecommerce']
