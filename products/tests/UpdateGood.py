from selenium import selenium
from django.test import TestCase
from django.test.client import Client
import unittest, time, re

from products.models import Good

class UpdateGood(TestCase):

	fixtures=['login_data.json']

	def setUp(self):
		self.c = Client()
		self.c.login(username='jimbarrows', password='newpass')
		self.existingGood = Good()
		self.existingGood.name="Existing Good"
		Good.objects.save( self.existingGood)
    	
	def test_update_good(self):
		response = self.c.get("/products/goods/add")
		self.failUnlessEqual(response.status_code, 200)
		response = self.c.post("/products/goods/save", {
			'categories-0-category_type':'' 
			,'categories-0-comment':'' 
			,'categories-0-from_date':'2010-12-24' 
			,'categories-0-id':'' 
			,'categories-0-product':'' 
			,'categories-0-thru_date':'' 
			,'categories-INITIAL_FORMS':'0' 
			,'categories-MAX_NUM_FORMS':'' 
			,'categories-TOTAL_FORMS':'1' 
			,'comment':'' 
			,'introduction_date':'' 
			,'manufactured_by':'' 
			,'name': self.existingGood.name
			,'sales_discontinuation_date':'' 
			,'supplier-0-available_from':'2010-12-24' 
			,'supplier-0-available_thru':'' 
			,'supplier-0-id':'' 
			,'supplier-0-organization':'' 
			,'supplier-0-product':'' 
			,'supplier-0-rating':'' 
			,'supplier-0-standard_lead_time_in_days':'' 
			,'supplier-INITIAL_FORMS':'0' 
			,'supplier-MAX_NUM_FORMS':'' 
			,'supplier-TOTAL_FORMS':'1' 
			,'support_discontinuation_date':'' }, follow=True)
		self.failUnlessEqual(response.status_code, 200)
		good = Good.objects.get( name__exact=(self.existingGood.name))
		self.assertEquals( good.name,self.existingGood.name)
    
	def tearDown(self):
		pass

if __name__ == "__main__":
    unittest.main()
