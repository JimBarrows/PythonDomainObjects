# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Order'
        db.create_table('orders_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_orders.order_set', null=True, to=orm['contenttypes.ContentType'])),
            ('order_date', self.gf('django.db.models.fields.DateField')()),
            ('entry_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('orders', ['Order'])

        # Adding model 'PurchaseOrder'
        db.create_table('orders_purchaseorder', (
            ('order_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['orders.Order'], unique=True, primary_key=True)),
            ('placed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='placingCustomerPo_set', to=orm['party.PartyRole'])),
            ('taken_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='internalOrganizationPo_set', to=orm['party.PartyRole'])),
            ('requested_bill_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='billToCustomerPo_set', to=orm['party.PartyRole'])),
            ('placing_location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='placing_locationPo_set', to=orm['party.ContactMechanism'])),
            ('location_for_taking', self.gf('django.db.models.fields.related.ForeignKey')(related_name='location_for_takingPo_set', to=orm['party.ContactMechanism'])),
            ('billed_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='billed_to_set', to=orm['party.ContactMechanism'])),
        ))
        db.send_create_signal('orders', ['PurchaseOrder'])

        # Adding model 'SalesOrder'
        db.create_table('orders_salesorder', (
            ('order_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['orders.Order'], unique=True, primary_key=True)),
            ('placed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='placingCustomerSo_set', to=orm['party.PartyRole'])),
            ('taken_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='internalOrganizationSo_set', to=orm['party.PartyRole'])),
            ('requested_bill_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='billToCustomerSo_set', to=orm['party.PartyRole'])),
            ('placing_location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='placing_locationSo_set', to=orm['party.ContactMechanism'])),
            ('location_for_taking', self.gf('django.db.models.fields.related.ForeignKey')(related_name='location_for_takingSo_set', to=orm['party.ContactMechanism'])),
            ('billed_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='billed_toSo_set', to=orm['party.ContactMechanism'])),
        ))
        db.send_create_signal('orders', ['SalesOrder'])

        # Adding model 'OrderItem'
        db.create_table('orders_orderitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unit_price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('estimated_delivery_date', self.gf('django.db.models.fields.DateField')()),
            ('shipping_instructions', self.gf('django.db.models.fields.TextField')()),
            ('item_description', self.gf('django.db.models.fields.TextField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('ordered_with', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_set', null=True, to=orm['orders.OrderItem'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('product_feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Feature'])),
        ))
        db.send_create_signal('orders', ['OrderItem'])

        # Adding model 'PurchaseOrderItem'
        db.create_table('orders_purchaseorderitem', (
            ('orderitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['orders.OrderItem'], unique=True, primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.PurchaseOrder'])),
            ('ship_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.ContactMechanism'])),
            ('ship_to_customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PartyRole'])),
        ))
        db.send_create_signal('orders', ['PurchaseOrderItem'])

        # Adding model 'SalesOrderItem'
        db.create_table('orders_salesorderitem', (
            ('orderitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['orders.OrderItem'], unique=True, primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.SalesOrder'])),
            ('ship_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.ContactMechanism'])),
            ('ship_to_customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PartyRole'])),
        ))
        db.send_create_signal('orders', ['SalesOrderItem'])

        # Adding M2M table for field purchased_by on 'SalesOrderItem'
        db.create_table('orders_salesorderitem_purchased_by', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('salesorderitem', models.ForeignKey(orm['orders.salesorderitem'], null=False)),
            ('purchaseorderitem', models.ForeignKey(orm['orders.purchaseorderitem'], null=False))
        ))
        db.create_unique('orders_salesorderitem_purchased_by', ['salesorderitem_id', 'purchaseorderitem_id'])

        # Adding model 'OrderRole'
        db.create_table('orders_orderrole', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('percent_contribution', self.gf('django.db.models.fields.IntegerField')()),
            ('of', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Order'])),
            ('involving', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
            ('described_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.OrderRoleType'])),
        ))
        db.send_create_signal('orders', ['OrderRole'])

        # Adding model 'OrderRoleType'
        db.create_table('orders_orderroletype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('orders', ['OrderRoleType'])

        # Adding model 'OrderAdjustment'
        db.create_table('orders_orderadjustment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('percentage', self.gf('django.db.models.fields.IntegerField')()),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.OrderRoleType'])),
            ('affectingItem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.OrderItem'])),
            ('affectingOrder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Order'])),
        ))
        db.send_create_signal('orders', ['OrderAdjustment'])

        # Adding model 'SalesTaxLookup'
        db.create_table('orders_salestaxlookup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geographicBoundary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.GeographicBoundary'])),
            ('productCategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
            ('percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal('orders', ['SalesTaxLookup'])

        # Adding model 'OrderAdjustmentType'
        db.create_table('orders_orderadjustmenttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('orders', ['OrderAdjustmentType'])

        # Adding model 'OrderTerm'
        db.create_table('orders_orderterm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('conditionForItem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.OrderItem'])),
            ('conditionForOrder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Order'])),
            ('described_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.OrderTermType'])),
        ))
        db.send_create_signal('orders', ['OrderTerm'])

        # Adding model 'OrderTermType'
        db.create_table('orders_ordertermtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('orders', ['OrderTermType'])

        # Adding model 'OrderStatus'
        db.create_table('orders_orderstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('conditionForItem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.OrderItem'])),
            ('conditionForOrder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Order'])),
            ('described_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.OrderStatusType'])),
        ))
        db.send_create_signal('orders', ['OrderStatus'])

        # Adding model 'OrderStatusType'
        db.create_table('orders_orderstatustype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('orders', ['OrderStatusType'])


    def backwards(self, orm):
        
        # Deleting model 'Order'
        db.delete_table('orders_order')

        # Deleting model 'PurchaseOrder'
        db.delete_table('orders_purchaseorder')

        # Deleting model 'SalesOrder'
        db.delete_table('orders_salesorder')

        # Deleting model 'OrderItem'
        db.delete_table('orders_orderitem')

        # Deleting model 'PurchaseOrderItem'
        db.delete_table('orders_purchaseorderitem')

        # Deleting model 'SalesOrderItem'
        db.delete_table('orders_salesorderitem')

        # Removing M2M table for field purchased_by on 'SalesOrderItem'
        db.delete_table('orders_salesorderitem_purchased_by')

        # Deleting model 'OrderRole'
        db.delete_table('orders_orderrole')

        # Deleting model 'OrderRoleType'
        db.delete_table('orders_orderroletype')

        # Deleting model 'OrderAdjustment'
        db.delete_table('orders_orderadjustment')

        # Deleting model 'SalesTaxLookup'
        db.delete_table('orders_salestaxlookup')

        # Deleting model 'OrderAdjustmentType'
        db.delete_table('orders_orderadjustmenttype')

        # Deleting model 'OrderTerm'
        db.delete_table('orders_orderterm')

        # Deleting model 'OrderTermType'
        db.delete_table('orders_ordertermtype')

        # Deleting model 'OrderStatus'
        db.delete_table('orders_orderstatus')

        # Deleting model 'OrderStatusType'
        db.delete_table('orders_orderstatustype')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'orders.order': {
            'Meta': {'object_name': 'Order'},
            'entry_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_orders.order_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"})
        },
        'orders.orderadjustment': {
            'Meta': {'object_name': 'OrderAdjustment'},
            'affectingItem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.OrderItem']"}),
            'affectingOrder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Order']"}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.OrderRoleType']"}),
            'percentage': ('django.db.models.fields.IntegerField', [], {})
        },
        'orders.orderadjustmenttype': {
            'Meta': {'object_name': 'OrderAdjustmentType'},
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
        'orders.orderrole': {
            'Meta': {'object_name': 'OrderRole'},
            'described_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.OrderRoleType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'involving': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'of': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Order']"}),
            'percent_contribution': ('django.db.models.fields.IntegerField', [], {})
        },
        'orders.orderroletype': {
            'Meta': {'object_name': 'OrderRoleType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'orders.orderstatus': {
            'Meta': {'object_name': 'OrderStatus'},
            'conditionForItem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.OrderItem']"}),
            'conditionForOrder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Order']"}),
            'described_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.OrderStatusType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        'orders.orderstatustype': {
            'Meta': {'object_name': 'OrderStatusType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'orders.orderterm': {
            'Meta': {'object_name': 'OrderTerm'},
            'conditionForItem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.OrderItem']"}),
            'conditionForOrder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Order']"}),
            'described_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.OrderTermType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        'orders.ordertermtype': {
            'Meta': {'object_name': 'OrderTermType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'orders.purchaseorder': {
            'Meta': {'object_name': 'PurchaseOrder', '_ormbases': ['orders.Order']},
            'billed_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'billed_to_set'", 'to': "orm['party.ContactMechanism']"}),
            'location_for_taking': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_for_takingPo_set'", 'to': "orm['party.ContactMechanism']"}),
            'order_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['orders.Order']", 'unique': 'True', 'primary_key': 'True'}),
            'placed_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'placingCustomerPo_set'", 'to': "orm['party.PartyRole']"}),
            'placing_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'placing_locationPo_set'", 'to': "orm['party.ContactMechanism']"}),
            'requested_bill_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'billToCustomerPo_set'", 'to': "orm['party.PartyRole']"}),
            'taken_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'internalOrganizationPo_set'", 'to': "orm['party.PartyRole']"})
        },
        'orders.purchaseorderitem': {
            'Meta': {'object_name': 'PurchaseOrderItem', '_ormbases': ['orders.OrderItem']},
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.PurchaseOrder']"}),
            'orderitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['orders.OrderItem']", 'unique': 'True', 'primary_key': 'True'}),
            'ship_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.ContactMechanism']"}),
            'ship_to_customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyRole']"})
        },
        'orders.salesorder': {
            'Meta': {'object_name': 'SalesOrder', '_ormbases': ['orders.Order']},
            'billed_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'billed_toSo_set'", 'to': "orm['party.ContactMechanism']"}),
            'location_for_taking': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_for_takingSo_set'", 'to': "orm['party.ContactMechanism']"}),
            'order_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['orders.Order']", 'unique': 'True', 'primary_key': 'True'}),
            'placed_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'placingCustomerSo_set'", 'to': "orm['party.PartyRole']"}),
            'placing_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'placing_locationSo_set'", 'to': "orm['party.ContactMechanism']"}),
            'requested_bill_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'billToCustomerSo_set'", 'to': "orm['party.PartyRole']"}),
            'taken_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'internalOrganizationSo_set'", 'to': "orm['party.PartyRole']"})
        },
        'orders.salesorderitem': {
            'Meta': {'object_name': 'SalesOrderItem', '_ormbases': ['orders.OrderItem']},
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.SalesOrder']"}),
            'orderitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['orders.OrderItem']", 'unique': 'True', 'primary_key': 'True'}),
            'purchased_by': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['orders.PurchaseOrderItem']", 'symmetrical': 'False'}),
            'ship_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.ContactMechanism']"}),
            'ship_to_customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyRole']"})
        },
        'orders.salestaxlookup': {
            'Meta': {'object_name': 'SalesTaxLookup'},
            'geographicBoundary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.GeographicBoundary']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'productCategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"})
        },
        'party.contactmechanism': {
            'Meta': {'object_name': 'ContactMechanism'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'party.geographicboundary': {
            'Meta': {'object_name': 'GeographicBoundary'},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'geocode': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'geographic_boundary_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.GeographicBoundaryType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        'party.geographicboundarytype': {
            'Meta': {'object_name': 'GeographicBoundaryType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 6, 42, 446188)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'party_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.partyrole': {
            'Meta': {'object_name': 'PartyRole'},
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 6, 42, 447975)'}),
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 6, 42, 544979)'}),
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 6, 42, 554178)'}),
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 6, 42, 557802)'}),
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
            'available_from': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 8, 21, 6, 42, 541969)'}),
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

    complete_apps = ['orders']
