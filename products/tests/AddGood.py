from selenium import selenium
from django.test import TestCase
from django.test.client import Client
import unittest, time, re

from products.models import Good

class AddGood(TestCase):

	fixtures=['login_data.json']

	def setUp(self):
		self.c = Client()
		self.c.login(username='jimbarrows', password='newpass')
		self.good =  Good()
		self.good.name = 'test_good'
    	
	def test_add_good(self):
		response = self.c.get("/products/goods/add")
		self.failUnlessEqual(response.status_code, 200)
		response = self.c.post("/products/goods/save", { 'name': self.good.name ,'introduction_date':'' ,'sales_discontinuation_date':'' ,'support_discontinuation_date':'' ,'manufactured_by':'' ,'comment':'' ,'categories-TOTAL_FORMS':'1' ,'categories-INITIAL_FORMS':'0' ,'categories-MAX_NUM_FORMS':'' ,'categories-0-product':'' ,'categories-0-id':'' ,'categories-0-category_type':'' ,'categories-0-from_date':'2010-12-24' ,'categories-0-thru_date':'' ,'categories-0-comment':'' ,'supplier-TOTAL_FORMS':'1' ,'supplier-INITIAL_FORMS':'0' ,'supplier-MAX_NUM_FORMS':'' ,'supplier-0-product':'' ,'supplier-0-id':'' ,'supplier-0-organization':'' ,'supplier-0-available_from':'2010-12-24' ,'supplier-0-available_thru':'' ,'supplier-0-standard_lead_time_in_days':'' ,'supplier-0-rating':'' } , follow=True)
		self.failUnlessEqual(response.status_code, 200)
		good = Good.objects.get( name__exact=(self.good.name))
		self.assertEquals( good.name, self.good.name)
    
	def tearDown(self):
		pass

if __name__ == "__main__":
    unittest.main()
