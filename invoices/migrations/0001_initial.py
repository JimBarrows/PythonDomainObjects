# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Invoice'
        db.create_table('invoices_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_invoices.invoice_set', null=True, to=orm['contenttypes.ContentType'])),
            ('invoice_date', self.gf('django.db.models.fields.DateField')()),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('billed_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='billedTo_set', to=orm['party.Party'])),
            ('billed_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='billedFrom_set', to=orm['party.Party'])),
            ('addressed_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='addressedTo_set', to=orm['party.ContactMechanism'])),
            ('addressed_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='addressedFrom_set', to=orm['party.ContactMechanism'])),
        ))
        db.send_create_signal('invoices', ['Invoice'])

        # Adding model 'SalesInvoice'
        db.create_table('invoices_salesinvoice', (
            ('invoice_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.Invoice'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('invoices', ['SalesInvoice'])

        # Adding model 'PurchaseInvoice'
        db.create_table('invoices_purchaseinvoice', (
            ('invoice_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.Invoice'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('invoices', ['PurchaseInvoice'])

        # Adding model 'Item'
        db.create_table('invoices_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_invoices.item_set', null=True, to=orm['contenttypes.ContentType'])),
            ('taxable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('invoices', ['Item'])

        # Adding model 'AcquiringItem'
        db.create_table('invoices_acquiringitem', (
            ('item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.Item'], unique=True, primary_key=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.Invoice'])),
        ))
        db.send_create_signal('invoices', ['AcquiringItem'])

        # Adding model 'ProductItem'
        db.create_table('invoices_productitem', (
            ('item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.Item'], unique=True, primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'], null=True, blank=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.Invoice'])),
        ))
        db.send_create_signal('invoices', ['ProductItem'])

        # Adding model 'FeatureItem'
        db.create_table('invoices_featureitem', (
            ('item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.Item'], unique=True, primary_key=True)),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Feature'], null=True, blank=True)),
            ('invoice_product_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.ProductItem'], null=True, blank=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.Invoice'])),
        ))
        db.send_create_signal('invoices', ['FeatureItem'])

        # Adding model 'Adjustment'
        db.create_table('invoices_adjustment', (
            ('item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.Item'], unique=True, primary_key=True)),
            ('perentage', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.Invoice'])),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.AdjustmentType'])),
        ))
        db.send_create_signal('invoices', ['Adjustment'])

        # Adding model 'AdjustmentType'
        db.create_table('invoices_adjustmenttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('invoices', ['AdjustmentType'])

        # Adding model 'PurchaseInvoiceItem'
        db.create_table('invoices_purchaseinvoiceitem', (
            ('item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.Item'], unique=True, primary_key=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.PurchaseInvoice'])),
        ))
        db.send_create_signal('invoices', ['PurchaseInvoiceItem'])

        # Adding model 'SalesInvoiceItem'
        db.create_table('invoices_salesinvoiceitem', (
            ('item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.Item'], unique=True, primary_key=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.SalesInvoice'])),
        ))
        db.send_create_signal('invoices', ['SalesInvoiceItem'])

        # Adding model 'RoleType'
        db.create_table('invoices_roletype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('invoices', ['RoleType'])

        # Adding model 'Role'
        db.create_table('invoices_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.Invoice'])),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
            ('role_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.RoleType'])),
            ('percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('invoices', ['Role'])

        # Adding model 'OrderItemBilling'
        db.create_table('invoices_orderitembilling', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invoice_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.Item'])),
            ('order_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.OrderItem'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal('invoices', ['OrderItemBilling'])

        # Adding model 'TermType'
        db.create_table('invoices_termtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('invoices', ['TermType'])

        # Adding model 'Term'
        db.create_table('invoices_term', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.TermType'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.Item'])),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.Invoice'])),
        ))
        db.send_create_signal('invoices', ['Term'])

        # Adding model 'StatusType'
        db.create_table('invoices_statustype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('invoices', ['StatusType'])

        # Adding model 'Status'
        db.create_table('invoices_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.Invoice'])),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.StatusType'])),
        ))
        db.send_create_signal('invoices', ['Status'])

        # Adding model 'PaymentMethodType'
        db.create_table('invoices_paymentmethodtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('invoices', ['PaymentMethodType'])

        # Adding model 'BillingAccount'
        db.create_table('invoices_billingaccount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('invoices', ['BillingAccount'])

        # Adding model 'Payment'
        db.create_table('invoices_payment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_invoices.payment_set', null=True, to=orm['contenttypes.ContentType'])),
            ('effective_date', self.gf('django.db.models.fields.DateField')()),
            ('reference_number', self.gf('django.db.models.fields.IntegerField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('paid_via', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.PaymentMethodType'])),
            ('paid_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='paidFrom_set', to=orm['party.Party'])),
            ('paid_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='paidTo_set', to=orm['party.Party'])),
        ))
        db.send_create_signal('invoices', ['Payment'])

        # Adding model 'Receipt'
        db.create_table('invoices_receipt', (
            ('payment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.Payment'], unique=True, primary_key=True)),
            ('deposit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.Deposit'])),
        ))
        db.send_create_signal('invoices', ['Receipt'])

        # Adding model 'Disbursement'
        db.create_table('invoices_disbursement', (
            ('payment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.Payment'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('invoices', ['Disbursement'])

        # Adding model 'PaymentApplication'
        db.create_table('invoices_paymentapplication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.Invoice'])),
            ('payment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.Payment'])),
            ('applied_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.BillingAccount'])),
            ('amount_applied', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal('invoices', ['PaymentApplication'])

        # Adding model 'FinancialAccountRoleType'
        db.create_table('invoices_financialaccountroletype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('invoices', ['FinancialAccountRoleType'])

        # Adding model 'FinancialAccountRole'
        db.create_table('invoices_financialaccountrole', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.FinancialAccountRoleType'])),
            ('from_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2010, 12, 11, 12, 41, 58, 69050))),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.FinancialAccount'])),
        ))
        db.send_create_signal('invoices', ['FinancialAccountRole'])

        # Adding model 'FinancialAccountType'
        db.create_table('invoices_financialaccounttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('invoices', ['FinancialAccountType'])

        # Adding model 'FinancialAccount'
        db.create_table('invoices_financialaccount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.FinancialAccountType'])),
        ))
        db.send_create_signal('invoices', ['FinancialAccount'])

        # Adding model 'FinancialAccountTransaction'
        db.create_table('invoices_financialaccounttransaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_invoices.financialaccounttransaction_set', null=True, to=orm['contenttypes.ContentType'])),
            ('transaction_date', self.gf('django.db.models.fields.DateField')()),
            ('entry_date', self.gf('django.db.models.fields.DateField')()),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoices.FinancialAccount'])),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Party'])),
        ))
        db.send_create_signal('invoices', ['FinancialAccountTransaction'])

        # Adding model 'Withdrawal'
        db.create_table('invoices_withdrawal', (
            ('financialaccounttransaction_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.FinancialAccountTransaction'], unique=True, primary_key=True)),
            ('disbursement', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.Disbursement'], unique=True)),
        ))
        db.send_create_signal('invoices', ['Withdrawal'])

        # Adding model 'Deposit'
        db.create_table('invoices_deposit', (
            ('financialaccounttransaction_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.FinancialAccountTransaction'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('invoices', ['Deposit'])

        # Adding model 'FinancialAccountAdjustment'
        db.create_table('invoices_financialaccountadjustment', (
            ('financialaccounttransaction_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['invoices.FinancialAccountTransaction'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('invoices', ['FinancialAccountAdjustment'])


    def backwards(self, orm):
        
        # Deleting model 'Invoice'
        db.delete_table('invoices_invoice')

        # Deleting model 'SalesInvoice'
        db.delete_table('invoices_salesinvoice')

        # Deleting model 'PurchaseInvoice'
        db.delete_table('invoices_purchaseinvoice')

        # Deleting model 'Item'
        db.delete_table('invoices_item')

        # Deleting model 'AcquiringItem'
        db.delete_table('invoices_acquiringitem')

        # Deleting model 'ProductItem'
        db.delete_table('invoices_productitem')

        # Deleting model 'FeatureItem'
        db.delete_table('invoices_featureitem')

        # Deleting model 'Adjustment'
        db.delete_table('invoices_adjustment')

        # Deleting model 'AdjustmentType'
        db.delete_table('invoices_adjustmenttype')

        # Deleting model 'PurchaseInvoiceItem'
        db.delete_table('invoices_purchaseinvoiceitem')

        # Deleting model 'SalesInvoiceItem'
        db.delete_table('invoices_salesinvoiceitem')

        # Deleting model 'RoleType'
        db.delete_table('invoices_roletype')

        # Deleting model 'Role'
        db.delete_table('invoices_role')

        # Deleting model 'OrderItemBilling'
        db.delete_table('invoices_orderitembilling')

        # Deleting model 'TermType'
        db.delete_table('invoices_termtype')

        # Deleting model 'Term'
        db.delete_table('invoices_term')

        # Deleting model 'StatusType'
        db.delete_table('invoices_statustype')

        # Deleting model 'Status'
        db.delete_table('invoices_status')

        # Deleting model 'PaymentMethodType'
        db.delete_table('invoices_paymentmethodtype')

        # Deleting model 'BillingAccount'
        db.delete_table('invoices_billingaccount')

        # Deleting model 'Payment'
        db.delete_table('invoices_payment')

        # Deleting model 'Receipt'
        db.delete_table('invoices_receipt')

        # Deleting model 'Disbursement'
        db.delete_table('invoices_disbursement')

        # Deleting model 'PaymentApplication'
        db.delete_table('invoices_paymentapplication')

        # Deleting model 'FinancialAccountRoleType'
        db.delete_table('invoices_financialaccountroletype')

        # Deleting model 'FinancialAccountRole'
        db.delete_table('invoices_financialaccountrole')

        # Deleting model 'FinancialAccountType'
        db.delete_table('invoices_financialaccounttype')

        # Deleting model 'FinancialAccount'
        db.delete_table('invoices_financialaccount')

        # Deleting model 'FinancialAccountTransaction'
        db.delete_table('invoices_financialaccounttransaction')

        # Deleting model 'Withdrawal'
        db.delete_table('invoices_withdrawal')

        # Deleting model 'Deposit'
        db.delete_table('invoices_deposit')

        # Deleting model 'FinancialAccountAdjustment'
        db.delete_table('invoices_financialaccountadjustment')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'invoices.acquiringitem': {
            'Meta': {'object_name': 'AcquiringItem', '_ormbases': ['invoices.Item']},
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']"}),
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.Item']", 'unique': 'True', 'primary_key': 'True'})
        },
        'invoices.adjustment': {
            'Meta': {'object_name': 'Adjustment', '_ormbases': ['invoices.Item']},
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']"}),
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.AdjustmentType']"}),
            'perentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        'invoices.adjustmenttype': {
            'Meta': {'object_name': 'AdjustmentType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'invoices.billingaccount': {
            'Meta': {'object_name': 'BillingAccount'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thru_date': ('django.db.models.fields.DateField', [], {})
        },
        'invoices.deposit': {
            'Meta': {'object_name': 'Deposit', '_ormbases': ['invoices.FinancialAccountTransaction']},
            'financialaccounttransaction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.FinancialAccountTransaction']", 'unique': 'True', 'primary_key': 'True'})
        },
        'invoices.disbursement': {
            'Meta': {'object_name': 'Disbursement', '_ormbases': ['invoices.Payment']},
            'payment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.Payment']", 'unique': 'True', 'primary_key': 'True'})
        },
        'invoices.featureitem': {
            'Meta': {'object_name': 'FeatureItem', '_ormbases': ['invoices.Item']},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Feature']", 'null': 'True', 'blank': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']"}),
            'invoice_product_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.ProductItem']", 'null': 'True', 'blank': 'True'}),
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.Item']", 'unique': 'True', 'primary_key': 'True'})
        },
        'invoices.financialaccount': {
            'Meta': {'object_name': 'FinancialAccount'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.FinancialAccountType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'owned_by': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['party.Party']", 'null': 'True', 'through': "orm['invoices.FinancialAccountRole']", 'blank': 'True'})
        },
        'invoices.financialaccountadjustment': {
            'Meta': {'object_name': 'FinancialAccountAdjustment', '_ormbases': ['invoices.FinancialAccountTransaction']},
            'financialaccounttransaction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.FinancialAccountTransaction']", 'unique': 'True', 'primary_key': 'True'})
        },
        'invoices.financialaccountrole': {
            'Meta': {'object_name': 'FinancialAccountRole'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.FinancialAccount']"}),
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 11, 12, 41, 58, 69050)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.FinancialAccountRoleType']"}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'invoices.financialaccountroletype': {
            'Meta': {'object_name': 'FinancialAccountRoleType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'invoices.financialaccounttransaction': {
            'Meta': {'object_name': 'FinancialAccountTransaction'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.FinancialAccount']"}),
            'entry_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_invoices.financialaccounttransaction_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'transaction_date': ('django.db.models.fields.DateField', [], {})
        },
        'invoices.financialaccounttype': {
            'Meta': {'object_name': 'FinancialAccountType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'invoices.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'addressed_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'addressedFrom_set'", 'to': "orm['party.ContactMechanism']"}),
            'addressed_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'addressedTo_set'", 'to': "orm['party.ContactMechanism']"}),
            'billed_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'billedFrom_set'", 'to': "orm['party.Party']"}),
            'billed_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'billedTo_set'", 'to': "orm['party.Party']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_date': ('django.db.models.fields.DateField', [], {}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'paid_via': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['invoices.Payment']", 'null': 'True', 'through': "orm['invoices.PaymentApplication']", 'blank': 'True'}),
            'parties': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['party.Party']", 'null': 'True', 'through': "orm['invoices.Role']", 'blank': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_invoices.invoice_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"})
        },
        'invoices.item': {
            'Meta': {'object_name': 'Item'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_items': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['orders.OrderItem']", 'null': 'True', 'through': "orm['invoices.OrderItemBilling']", 'blank': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_invoices.item_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'taxable': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'invoices.orderitembilling': {
            'Meta': {'object_name': 'OrderItemBilling'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Item']"}),
            'order_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.OrderItem']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'invoices.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'effective_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'paidFrom_set'", 'to': "orm['party.Party']"}),
            'paid_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'paidTo_set'", 'to': "orm['party.Party']"}),
            'paid_via': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.PaymentMethodType']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_invoices.payment_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'reference_number': ('django.db.models.fields.IntegerField', [], {})
        },
        'invoices.paymentapplication': {
            'Meta': {'object_name': 'PaymentApplication'},
            'amount_applied': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'applied_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.BillingAccount']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']"}),
            'payment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Payment']"})
        },
        'invoices.paymentmethodtype': {
            'Meta': {'object_name': 'PaymentMethodType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'invoices.productitem': {
            'Meta': {'object_name': 'ProductItem', '_ormbases': ['invoices.Item']},
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']"}),
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']", 'null': 'True', 'blank': 'True'})
        },
        'invoices.purchaseinvoice': {
            'Meta': {'object_name': 'PurchaseInvoice', '_ormbases': ['invoices.Invoice']},
            'invoice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.Invoice']", 'unique': 'True', 'primary_key': 'True'})
        },
        'invoices.purchaseinvoiceitem': {
            'Meta': {'object_name': 'PurchaseInvoiceItem', '_ormbases': ['invoices.Item']},
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.PurchaseInvoice']"}),
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.Item']", 'unique': 'True', 'primary_key': 'True'})
        },
        'invoices.receipt': {
            'Meta': {'object_name': 'Receipt', '_ormbases': ['invoices.Payment']},
            'deposit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Deposit']"}),
            'payment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.Payment']", 'unique': 'True', 'primary_key': 'True'})
        },
        'invoices.role': {
            'Meta': {'object_name': 'Role'},
            'at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']"}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'role_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.RoleType']"})
        },
        'invoices.roletype': {
            'Meta': {'object_name': 'RoleType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'invoices.salesinvoice': {
            'Meta': {'object_name': 'SalesInvoice', '_ormbases': ['invoices.Invoice']},
            'invoice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.Invoice']", 'unique': 'True', 'primary_key': 'True'})
        },
        'invoices.salesinvoiceitem': {
            'Meta': {'object_name': 'SalesInvoiceItem', '_ormbases': ['invoices.Item']},
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.SalesInvoice']"}),
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.Item']", 'unique': 'True', 'primary_key': 'True'})
        },
        'invoices.status': {
            'Meta': {'object_name': 'Status'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']"}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.StatusType']"})
        },
        'invoices.statustype': {
            'Meta': {'object_name': 'StatusType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'invoices.term': {
            'Meta': {'object_name': 'Term'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Invoice']"}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.Item']"}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoices.TermType']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'invoices.termtype': {
            'Meta': {'object_name': 'TermType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'invoices.withdrawal': {
            'Meta': {'object_name': 'Withdrawal', '_ormbases': ['invoices.FinancialAccountTransaction']},
            'disbursement': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.Disbursement']", 'unique': 'True'}),
            'financialaccounttransaction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['invoices.FinancialAccountTransaction']", 'unique': 'True', 'primary_key': 'True'})
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
        'party.contactmechanism': {
            'Meta': {'object_name': 'ContactMechanism'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 11, 12, 41, 57, 867099)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'party_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.partyrole': {
            'Meta': {'object_name': 'PartyRole'},
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 11, 12, 41, 57, 868539)'}),
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 11, 12, 41, 57, 958195)'}),
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 11, 12, 41, 57, 966278)'}),
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 11, 12, 41, 57, 969309)'}),
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
            'available_from': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2010, 12, 11, 12, 41, 57, 955110)'}),
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

    complete_apps = ['invoices']
