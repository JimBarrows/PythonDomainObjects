from selenium import selenium
import unittest, time, re

class InitialSetup(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://localhost:8000/")
        self.selenium.start()
    
    def test_initial_setup(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=Business")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Main Organization: NSFW Enterrises, LLC", sel.get_text("//div[@id='content']/h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        self.assertEqual("NSFW Enterprises, LLC - Business", sel.get_title())
        sel.type("id_name", "Biz On Demand")
        sel.click("id_date_started")
        sel.type("id_date_started", "10/10/2010")
        sel.select("id_sub_org_role", "label=DBA")
        sel.click("//input[@value='Add']")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Biz On Demand", sel.get_text("//div[@id='content']/div[2]/ul[2]/li"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
