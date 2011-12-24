# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Product'
        db.create_table('products_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_products.product_set', null=True, to=orm['contenttypes.ContentType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('introduction_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('sales_discontinuation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('support_discontinuation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('manufactured_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='producerOf_set', null=True, to=orm['party.Organization'])),
        ))
        db.send_create_signal('products', ['Product'])

        # Adding model 'Good'
        db.create_table('products_good', (
            ('product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.Product'], unique=True, primary_key=True)),
            ('finished_good', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.FinishedGood'], null=True, blank=True)),
        ))
        db.send_create_signal('products', ['Good'])

        # Adding model 'Service'
        db.create_table('products_service', (
            ('product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.Product'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('products', ['Service'])

        # Adding model 'Part'
        db.create_table('products_part', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_products.part_set', null=True, to=orm['contenttypes.ContentType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('products', ['Part'])

        # Adding model 'FinishedGood'
        db.create_table('products_finishedgood', (
            ('part_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.Part'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('products', ['FinishedGood'])

        # Adding model 'SubAssembly'
        db.create_table('products_subassembly', (
            ('part_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.Part'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('products', ['SubAssembly'])

        # Adding model 'RawMaterial'
        db.create_table('products_rawmaterial', (
            ('part_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.Part'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('products', ['RawMaterial'])

        # Adding model 'PartBom'
        db.create_table('products_partbom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('quantity_used', self.gf('django.db.models.fields.IntegerField')()),
            ('instruction', self.gf('django.db.models.fields.TextField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('products', ['PartBom'])

        # Adding model 'ProductAssociation'
        db.create_table('products_productassociation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.ProductAssociationType'])),
            ('from_product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fromAssociation_set', to=orm['products.Product'])),
            ('to_product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='toAssociation_set', to=orm['products.Product'])),
        ))
        db.send_create_signal('products', ['ProductAssociation'])

        # Adding model 'ProductAssociationType'
        db.create_table('products_productassociationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('products', ['ProductAssociationType'])

        # Adding model 'EstimatedProductCost'
        db.create_table('products_estimatedproductcost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_products.estimatedproductcost_set', null=True, to=orm['contenttypes.ContentType'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Feature'], null=True, blank=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'], null=True, blank=True)),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.CostComponentType'])),
            ('geographic_boundary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.GeographicBoundary'], null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='estimatedProductCost_set', to=orm['party.Organization'])),
        ))
        db.send_create_signal('products', ['EstimatedProductCost'])

        # Adding model 'CostComponentType'
        db.create_table('products_costcomponenttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('products', ['CostComponentType'])

        # Adding model 'PriceComponent'
        db.create_table('products_pricecomponent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_products.pricecomponent_set', null=True, to=orm['contenttypes.ContentType'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'], null=True, blank=True)),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('geographic_boundary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.GeographicBoundary'], null=True, blank=True)),
            ('party_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PartyType'], null=True, blank=True)),
            ('product_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'], null=True, blank=True)),
            ('quantity_break', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.QuantityBreak'], null=True, blank=True)),
            ('order_value', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.OrderValue'], null=True, blank=True)),
            ('sales_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.SaleType'], null=True, blank=True)),
            ('specified_for', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Organization'], null=True, blank=True)),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Feature'], null=True, blank=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.CurrencyMeasure'], null=True, blank=True)),
            ('part', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Part'], null=True, blank=True)),
        ))
        db.send_create_signal('products', ['PriceComponent'])

        # Adding model 'BasePrice'
        db.create_table('products_baseprice', (
            ('pricecomponent_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.PriceComponent'], unique=True, primary_key=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('products', ['BasePrice'])

        # Adding model 'DiscountComponent'
        db.create_table('products_discountcomponent', (
            ('pricecomponent_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.PriceComponent'], unique=True, primary_key=True)),
            ('percent', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('products', ['DiscountComponent'])

        # Adding model 'SurchargeComponent'
        db.create_table('products_surchargecomponent', (
            ('pricecomponent_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.PriceComponent'], unique=True, primary_key=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('percent', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('products', ['SurchargeComponent'])

        # Adding model 'ManufacturerSuggestedPrice'
        db.create_table('products_manufacturersuggestedprice', (
            ('pricecomponent_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.PriceComponent'], unique=True, primary_key=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('products', ['ManufacturerSuggestedPrice'])

        # Adding model 'OneTimeCharge'
        db.create_table('products_onetimecharge', (
            ('pricecomponent_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.PriceComponent'], unique=True, primary_key=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('percent', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('products', ['OneTimeCharge'])

        # Adding model 'RecurringCharge'
        db.create_table('products_recurringcharge', (
            ('pricecomponent_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.PriceComponent'], unique=True, primary_key=True)),
            ('per', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.TimeFrequencyMeasure'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('products', ['RecurringCharge'])

        # Adding model 'UtilizationCharge'
        db.create_table('products_utilizationcharge', (
            ('pricecomponent_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.PriceComponent'], unique=True, primary_key=True)),
            ('per', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.UnitOfMeasure'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('products', ['UtilizationCharge'])

        # Adding model 'SaleType'
        db.create_table('products_saletype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('products', ['SaleType'])

        # Adding model 'OrderValue'
        db.create_table('products_ordervalue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_value', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('thru_value', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal('products', ['OrderValue'])

        # Adding model 'QuantityBreak'
        db.create_table('products_quantitybreak', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('thru_quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('products', ['QuantityBreak'])

        # Adding model 'InventoryItem'
        db.create_table('products_inventoryitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_products.inventoryitem_set', null=True, to=orm['contenttypes.ContentType'])),
            ('good', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Good'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.InventoryItemStatusType'])),
            ('located_at', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Facility'])),
            ('located_within', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Container'])),
            ('part', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Part'])),
            ('lot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Lot'])),
        ))
        db.send_create_signal('products', ['InventoryItem'])

        # Adding model 'SerializedInventoryItem'
        db.create_table('products_serializedinventoryitem', (
            ('inventoryitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.InventoryItem'], unique=True, primary_key=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('products', ['SerializedInventoryItem'])

        # Adding model 'NonSerializedInventoryItem'
        db.create_table('products_nonserializedinventoryitem', (
            ('inventoryitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.InventoryItem'], unique=True, primary_key=True)),
            ('quantity_on_hand', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('products', ['NonSerializedInventoryItem'])

        # Adding model 'InventoryItemVariance'
        db.create_table('products_inventoryitemvariance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('physical_inventory_date', self.gf('django.db.models.fields.DateField')()),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('reason', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Reason'])),
            ('adjustment_for', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.InventoryItem'])),
        ))
        db.send_create_signal('products', ['InventoryItemVariance'])

        # Adding model 'Reason'
        db.create_table('products_reason', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('products', ['Reason'])

        # Adding model 'Container'
        db.create_table('products_container', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('located_at', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Facility'])),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.ContainerType'])),
        ))
        db.send_create_signal('products', ['Container'])

        # Adding model 'ContainerType'
        db.create_table('products_containertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('products', ['ContainerType'])

        # Adding model 'Lot'
        db.create_table('products_lot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('creation_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2011, 12, 24, 1, 14, 35, 776426))),
            ('expiration_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('products', ['Lot'])

        # Adding model 'InventoryItemStatusType'
        db.create_table('products_inventoryitemstatustype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('products', ['InventoryItemStatusType'])

        # Adding model 'ReorderGuideline'
        db.create_table('products_reorderguideline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guidelineFor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Good'])),
            ('from_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2011, 12, 24, 1, 14, 35, 780013))),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('reorder_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('reorder_level', self.gf('django.db.models.fields.IntegerField')()),
            ('boundary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.GeographicBoundary'])),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Facility'])),
            ('internal_organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PartyRole'])),
            ('part', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Part'])),
        ))
        db.send_create_signal('products', ['ReorderGuideline'])

        # Adding model 'SupplierProduct'
        db.create_table('products_supplierproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.Organization'])),
            ('available_from', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2011, 12, 24, 1, 14, 35, 781109))),
            ('available_thru', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('standard_lead_time_in_days', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('preference', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.PreferenceType'], null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.RatingType'], null=True, blank=True)),
            ('part', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Part'], null=True, blank=True)),
        ))
        db.send_create_signal('products', ['SupplierProduct'])

        # Adding model 'PreferenceType'
        db.create_table('products_preferencetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('products', ['PreferenceType'])

        # Adding model 'RatingType'
        db.create_table('products_ratingtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('products', ['RatingType'])

        # Adding model 'Identification'
        db.create_table('products_identification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('good', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Good'])),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.IdentificationType'])),
            ('from_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2011, 12, 24, 1, 14, 35, 783065))),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('products', ['Identification'])

        # Adding model 'CategoryClassification'
        db.create_table('products_categoryclassification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('category_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
            ('from_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2011, 12, 24, 1, 14, 35, 783804))),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('products', ['CategoryClassification'])

        # Adding model 'Feature'
        db.create_table('products_feature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_products.feature_set', null=True, to=orm['contenttypes.ContentType'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.FeatureCategory'])),
        ))
        db.send_create_signal('products', ['Feature'])

        # Adding model 'Dimension'
        db.create_table('products_dimension', (
            ('feature_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.Feature'], unique=True, primary_key=True)),
            ('number_specified', self.gf('django.db.models.fields.IntegerField')()),
            ('measured_using', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.UnitOfMeasure'])),
        ))
        db.send_create_signal('products', ['Dimension'])

        # Adding model 'UnitOfMeasure'
        db.create_table('products_unitofmeasure', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_products.unitofmeasure_set', null=True, to=orm['contenttypes.ContentType'])),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('products', ['UnitOfMeasure'])

        # Adding model 'TimeFrequencyMeasure'
        db.create_table('products_timefrequencymeasure', (
            ('unitofmeasure_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.UnitOfMeasure'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('products', ['TimeFrequencyMeasure'])

        # Adding model 'CurrencyMeasure'
        db.create_table('products_currencymeasure', (
            ('unitofmeasure_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['products.UnitOfMeasure'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('products', ['CurrencyMeasure'])

        # Adding model 'UnitOfMeasureConversion'
        db.create_table('products_unitofmeasureconversion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('convert_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='convert_from_set', to=orm['products.UnitOfMeasure'])),
            ('convert_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='convertInto_set', to=orm['products.UnitOfMeasure'])),
            ('conversion_factor', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=3)),
        ))
        db.send_create_signal('products', ['UnitOfMeasureConversion'])

        # Adding model 'FeatureApplicability'
        db.create_table('products_featureapplicability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2011, 12, 24, 1, 14, 35, 790919))),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Feature'])),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('products', ['FeatureApplicability'])

        # Adding model 'FeatureInteraction'
        db.create_table('products_featureinteraction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('incompatibility', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('interaction_dependancy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('of', self.gf('django.db.models.fields.related.ForeignKey')(related_name='of_set', to=orm['products.Feature'])),
            ('factor_in', self.gf('django.db.models.fields.related.ForeignKey')(related_name='factor_in_set', to=orm['products.Feature'])),
            ('context_of', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
        ))
        db.send_create_signal('products', ['FeatureInteraction'])

        # Adding model 'Category'
        db.create_table('products_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_set', null=True, to=orm['products.Category'])),
        ))
        db.send_create_signal('products', ['Category'])

        # Adding model 'MarketInterest'
        db.create_table('products_marketinterest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('party_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['party.PartyType'])),
            ('category_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Category'])),
            ('from_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2011, 12, 24, 1, 14, 35, 793586))),
            ('thru_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('products', ['MarketInterest'])

        # Adding model 'IdentificationType'
        db.create_table('products_identificationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('products', ['IdentificationType'])

        # Adding model 'FeatureCategory'
        db.create_table('products_featurecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('products', ['FeatureCategory'])


    def backwards(self, orm):
        
        # Deleting model 'Product'
        db.delete_table('products_product')

        # Deleting model 'Good'
        db.delete_table('products_good')

        # Deleting model 'Service'
        db.delete_table('products_service')

        # Deleting model 'Part'
        db.delete_table('products_part')

        # Deleting model 'FinishedGood'
        db.delete_table('products_finishedgood')

        # Deleting model 'SubAssembly'
        db.delete_table('products_subassembly')

        # Deleting model 'RawMaterial'
        db.delete_table('products_rawmaterial')

        # Deleting model 'PartBom'
        db.delete_table('products_partbom')

        # Deleting model 'ProductAssociation'
        db.delete_table('products_productassociation')

        # Deleting model 'ProductAssociationType'
        db.delete_table('products_productassociationtype')

        # Deleting model 'EstimatedProductCost'
        db.delete_table('products_estimatedproductcost')

        # Deleting model 'CostComponentType'
        db.delete_table('products_costcomponenttype')

        # Deleting model 'PriceComponent'
        db.delete_table('products_pricecomponent')

        # Deleting model 'BasePrice'
        db.delete_table('products_baseprice')

        # Deleting model 'DiscountComponent'
        db.delete_table('products_discountcomponent')

        # Deleting model 'SurchargeComponent'
        db.delete_table('products_surchargecomponent')

        # Deleting model 'ManufacturerSuggestedPrice'
        db.delete_table('products_manufacturersuggestedprice')

        # Deleting model 'OneTimeCharge'
        db.delete_table('products_onetimecharge')

        # Deleting model 'RecurringCharge'
        db.delete_table('products_recurringcharge')

        # Deleting model 'UtilizationCharge'
        db.delete_table('products_utilizationcharge')

        # Deleting model 'SaleType'
        db.delete_table('products_saletype')

        # Deleting model 'OrderValue'
        db.delete_table('products_ordervalue')

        # Deleting model 'QuantityBreak'
        db.delete_table('products_quantitybreak')

        # Deleting model 'InventoryItem'
        db.delete_table('products_inventoryitem')

        # Deleting model 'SerializedInventoryItem'
        db.delete_table('products_serializedinventoryitem')

        # Deleting model 'NonSerializedInventoryItem'
        db.delete_table('products_nonserializedinventoryitem')

        # Deleting model 'InventoryItemVariance'
        db.delete_table('products_inventoryitemvariance')

        # Deleting model 'Reason'
        db.delete_table('products_reason')

        # Deleting model 'Container'
        db.delete_table('products_container')

        # Deleting model 'ContainerType'
        db.delete_table('products_containertype')

        # Deleting model 'Lot'
        db.delete_table('products_lot')

        # Deleting model 'InventoryItemStatusType'
        db.delete_table('products_inventoryitemstatustype')

        # Deleting model 'ReorderGuideline'
        db.delete_table('products_reorderguideline')

        # Deleting model 'SupplierProduct'
        db.delete_table('products_supplierproduct')

        # Deleting model 'PreferenceType'
        db.delete_table('products_preferencetype')

        # Deleting model 'RatingType'
        db.delete_table('products_ratingtype')

        # Deleting model 'Identification'
        db.delete_table('products_identification')

        # Deleting model 'CategoryClassification'
        db.delete_table('products_categoryclassification')

        # Deleting model 'Feature'
        db.delete_table('products_feature')

        # Deleting model 'Dimension'
        db.delete_table('products_dimension')

        # Deleting model 'UnitOfMeasure'
        db.delete_table('products_unitofmeasure')

        # Deleting model 'TimeFrequencyMeasure'
        db.delete_table('products_timefrequencymeasure')

        # Deleting model 'CurrencyMeasure'
        db.delete_table('products_currencymeasure')

        # Deleting model 'UnitOfMeasureConversion'
        db.delete_table('products_unitofmeasureconversion')

        # Deleting model 'FeatureApplicability'
        db.delete_table('products_featureapplicability')

        # Deleting model 'FeatureInteraction'
        db.delete_table('products_featureinteraction')

        # Deleting model 'Category'
        db.delete_table('products_category')

        # Deleting model 'MarketInterest'
        db.delete_table('products_marketinterest')

        # Deleting model 'IdentificationType'
        db.delete_table('products_identificationtype')

        # Deleting model 'FeatureCategory'
        db.delete_table('products_featurecategory')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'party.contactmechanism': {
            'Meta': {'object_name': 'ContactMechanism'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 12, 24, 1, 14, 35, 704584)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Party']"}),
            'party_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'party.partyrole': {
            'Meta': {'object_name': 'PartyRole'},
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 12, 24, 1, 14, 35, 705885)'}),
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
        'products.baseprice': {
            'Meta': {'object_name': 'BasePrice', '_ormbases': ['products.PriceComponent']},
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'pricecomponent_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.PriceComponent']", 'unique': 'True', 'primary_key': 'True'})
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 12, 24, 1, 14, 35, 783804)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'products.container': {
            'Meta': {'object_name': 'Container'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.ContainerType']"}),
            'located_at': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Facility']"})
        },
        'products.containertype': {
            'Meta': {'object_name': 'ContainerType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.costcomponenttype': {
            'Meta': {'object_name': 'CostComponentType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.currencymeasure': {
            'Meta': {'ordering': "['abbreviation', 'description']", 'object_name': 'CurrencyMeasure', '_ormbases': ['products.UnitOfMeasure']},
            'unitofmeasure_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.UnitOfMeasure']", 'unique': 'True', 'primary_key': 'True'})
        },
        'products.dimension': {
            'Meta': {'object_name': 'Dimension', '_ormbases': ['products.Feature']},
            'feature_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.Feature']", 'unique': 'True', 'primary_key': 'True'}),
            'measured_using': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.UnitOfMeasure']"}),
            'number_specified': ('django.db.models.fields.IntegerField', [], {})
        },
        'products.discountcomponent': {
            'Meta': {'object_name': 'DiscountComponent', '_ormbases': ['products.PriceComponent']},
            'percent': ('django.db.models.fields.IntegerField', [], {}),
            'pricecomponent_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.PriceComponent']", 'unique': 'True', 'primary_key': 'True'})
        },
        'products.estimatedproductcost': {
            'Meta': {'object_name': 'EstimatedProductCost'},
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Feature']", 'null': 'True', 'blank': 'True'}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'geographic_boundary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.GeographicBoundary']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.CostComponentType']"}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'estimatedProductCost_set'", 'to': "orm['party.Organization']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_products.estimatedproductcost_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']", 'null': 'True', 'blank': 'True'}),
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
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 12, 24, 1, 14, 35, 790919)'}),
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
        'products.featureinteraction': {
            'Meta': {'object_name': 'FeatureInteraction'},
            'context_of': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'factor_in': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'factor_in_set'", 'to': "orm['products.Feature']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incompatibility': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interaction_dependancy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'of': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'of_set'", 'to': "orm['products.Feature']"})
        },
        'products.finishedgood': {
            'Meta': {'object_name': 'FinishedGood', '_ormbases': ['products.Part']},
            'part_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.Part']", 'unique': 'True', 'primary_key': 'True'})
        },
        'products.good': {
            'Meta': {'ordering': "['name']", 'object_name': 'Good', '_ormbases': ['products.Product']},
            'finished_good': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.FinishedGood']", 'null': 'True', 'blank': 'True'}),
            'identifiers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['products.IdentificationType']", 'null': 'True', 'through': "orm['products.Identification']", 'blank': 'True'}),
            'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.Product']", 'unique': 'True', 'primary_key': 'True'})
        },
        'products.identification': {
            'Meta': {'object_name': 'Identification'},
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 12, 24, 1, 14, 35, 783065)'}),
            'good': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Good']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.IdentificationType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'products.identificationtype': {
            'Meta': {'object_name': 'IdentificationType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.inventoryitem': {
            'Meta': {'object_name': 'InventoryItem'},
            'good': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Good']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'located_at': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Facility']"}),
            'located_within': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Container']"}),
            'lot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Lot']"}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Part']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_products.inventoryitem_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.InventoryItemStatusType']"})
        },
        'products.inventoryitemstatustype': {
            'Meta': {'object_name': 'InventoryItemStatusType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.inventoryitemvariance': {
            'Meta': {'object_name': 'InventoryItemVariance'},
            'adjustment_for': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.InventoryItem']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'physical_inventory_date': ('django.db.models.fields.DateField', [], {}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'reason': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Reason']"})
        },
        'products.lot': {
            'Meta': {'object_name': 'Lot'},
            'creation_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 12, 24, 1, 14, 35, 776426)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'expiration_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'products.manufacturersuggestedprice': {
            'Meta': {'object_name': 'ManufacturerSuggestedPrice', '_ormbases': ['products.PriceComponent']},
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'pricecomponent_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.PriceComponent']", 'unique': 'True', 'primary_key': 'True'})
        },
        'products.marketinterest': {
            'Meta': {'object_name': 'MarketInterest'},
            'category_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']"}),
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 12, 24, 1, 14, 35, 793586)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'products.nonserializedinventoryitem': {
            'Meta': {'object_name': 'NonSerializedInventoryItem', '_ormbases': ['products.InventoryItem']},
            'inventoryitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.InventoryItem']", 'unique': 'True', 'primary_key': 'True'}),
            'quantity_on_hand': ('django.db.models.fields.IntegerField', [], {})
        },
        'products.onetimecharge': {
            'Meta': {'object_name': 'OneTimeCharge', '_ormbases': ['products.PriceComponent']},
            'percent': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'pricecomponent_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.PriceComponent']", 'unique': 'True', 'primary_key': 'True'})
        },
        'products.ordervalue': {
            'Meta': {'object_name': 'OrderValue'},
            'from_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thru_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        },
        'products.part': {
            'Meta': {'object_name': 'Part'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_products.part_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"})
        },
        'products.partbom': {
            'Meta': {'object_name': 'PartBom'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.TextField', [], {}),
            'quantity_used': ('django.db.models.fields.IntegerField', [], {}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'products.preferencetype': {
            'Meta': {'object_name': 'PreferenceType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.pricecomponent': {
            'Meta': {'object_name': 'PriceComponent'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.CurrencyMeasure']", 'null': 'True', 'blank': 'True'}),
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Feature']", 'null': 'True', 'blank': 'True'}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'geographic_boundary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.GeographicBoundary']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_value': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.OrderValue']", 'null': 'True', 'blank': 'True'}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Part']", 'null': 'True', 'blank': 'True'}),
            'party_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyType']", 'null': 'True', 'blank': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_products.pricecomponent_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']", 'null': 'True', 'blank': 'True'}),
            'product_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Category']", 'null': 'True', 'blank': 'True'}),
            'quantity_break': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.QuantityBreak']", 'null': 'True', 'blank': 'True'}),
            'sales_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.SaleType']", 'null': 'True', 'blank': 'True'}),
            'specified_for': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Organization']", 'null': 'True', 'blank': 'True'}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
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
        'products.productassociation': {
            'Meta': {'object_name': 'ProductAssociation'},
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'from_product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fromAssociation_set'", 'to': "orm['products.Product']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.ProductAssociationType']"}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'to_product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'toAssociation_set'", 'to': "orm['products.Product']"})
        },
        'products.productassociationtype': {
            'Meta': {'object_name': 'ProductAssociationType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.quantitybreak': {
            'Meta': {'ordering': "['from_quantity', 'thru_quantity']", 'object_name': 'QuantityBreak'},
            'from_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thru_quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'products.ratingtype': {
            'Meta': {'object_name': 'RatingType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.rawmaterial': {
            'Meta': {'object_name': 'RawMaterial', '_ormbases': ['products.Part']},
            'part_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.Part']", 'unique': 'True', 'primary_key': 'True'})
        },
        'products.reason': {
            'Meta': {'object_name': 'Reason'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.recurringcharge': {
            'Meta': {'object_name': 'RecurringCharge', '_ormbases': ['products.PriceComponent']},
            'per': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.TimeFrequencyMeasure']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'pricecomponent_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.PriceComponent']", 'unique': 'True', 'primary_key': 'True'})
        },
        'products.reorderguideline': {
            'Meta': {'object_name': 'ReorderGuideline'},
            'boundary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.GeographicBoundary']"}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Facility']"}),
            'from_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 12, 24, 1, 14, 35, 780013)'}),
            'guidelineFor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Good']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.PartyRole']"}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Part']"}),
            'reorder_level': ('django.db.models.fields.IntegerField', [], {}),
            'reorder_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'thru_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'products.saletype': {
            'Meta': {'object_name': 'SaleType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.serializedinventoryitem': {
            'Meta': {'object_name': 'SerializedInventoryItem', '_ormbases': ['products.InventoryItem']},
            'inventoryitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.InventoryItem']", 'unique': 'True', 'primary_key': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'products.service': {
            'Meta': {'ordering': "['name']", 'object_name': 'Service', '_ormbases': ['products.Product']},
            'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.Product']", 'unique': 'True', 'primary_key': 'True'})
        },
        'products.subassembly': {
            'Meta': {'object_name': 'SubAssembly', '_ormbases': ['products.Part']},
            'part_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.Part']", 'unique': 'True', 'primary_key': 'True'})
        },
        'products.supplierproduct': {
            'Meta': {'object_name': 'SupplierProduct'},
            'available_from': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 12, 24, 1, 14, 35, 781109)'}),
            'available_thru': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['party.Organization']"}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Part']", 'null': 'True', 'blank': 'True'}),
            'preference': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.PreferenceType']", 'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'rating': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.RatingType']", 'null': 'True', 'blank': 'True'}),
            'standard_lead_time_in_days': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'products.surchargecomponent': {
            'Meta': {'object_name': 'SurchargeComponent', '_ormbases': ['products.PriceComponent']},
            'percent': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'pricecomponent_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.PriceComponent']", 'unique': 'True', 'primary_key': 'True'})
        },
        'products.timefrequencymeasure': {
            'Meta': {'ordering': "['abbreviation', 'description']", 'object_name': 'TimeFrequencyMeasure', '_ormbases': ['products.UnitOfMeasure']},
            'unitofmeasure_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.UnitOfMeasure']", 'unique': 'True', 'primary_key': 'True'})
        },
        'products.unitofmeasure': {
            'Meta': {'ordering': "['abbreviation', 'description']", 'object_name': 'UnitOfMeasure'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_products.unitofmeasure_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"})
        },
        'products.unitofmeasureconversion': {
            'Meta': {'object_name': 'UnitOfMeasureConversion'},
            'conversion_factor': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'}),
            'convert_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'convert_from_set'", 'to': "orm['products.UnitOfMeasure']"}),
            'convert_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'convertInto_set'", 'to': "orm['products.UnitOfMeasure']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'products.utilizationcharge': {
            'Meta': {'object_name': 'UtilizationCharge', '_ormbases': ['products.PriceComponent']},
            'per': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.UnitOfMeasure']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'pricecomponent_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['products.PriceComponent']", 'unique': 'True', 'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['products']
