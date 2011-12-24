from selenium import selenium
import unittest, time, re

class AddUpdateGood(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://localhost:8000/")
        self.selenium.start()
    
    def test_add_update_good(self):
        sel = self.selenium
        sel.open("/accounts/login/?next=/")
        try: self.failUnless(sel.is_text_present("Welcome to NSFW Enterprises, LLC"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        self.assertEqual("NSFW Enterprises, LLC - Login", sel.get_title())
        sel.type("id_username", "jimbarrows")
        sel.type("id_password", "newpass")
        sel.click("loginButton")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("NSFW Enterprises, LLC - Business Setup", sel.get_title())
        sel.type("id_name", "test biz")
        sel.click("//input[@value='Save']")
        sel.wait_for_page_to_load("30000")
        sel.click("products_link")
        sel.wait_for_page_to_load("30000")
        sel.click("add_good_link")
        sel.wait_for_page_to_load("30000")
        sel.type("id_name", "test good")
        sel.type("id_introduction_date", "01/01/2000")
        sel.type("id_sales_discontinuation_date", "01/01/2020")
        sel.type("id_support_discontinuation_date", "01/01/2021")
        sel.type("id_comment", "This is a comment")
        sel.click("save_button")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("test good", sel.get_table("//div[@id='content']/div/table[1].1.0"))
        self.assertEqual("NSFW Enterprises, LLC - Goods Services", sel.get_title())
        sel.click("link=test good")
        sel.wait_for_page_to_load("30000")
        sel.type("id_name", "test good 2")
        sel.type("id_introduction_date", "2000-01-02")
        sel.type("id_sales_discontinuation_date", "2020-01-02")
        sel.type("id_support_discontinuation_date", "2021-01-02")
        sel.type("id_comment", "This is a comment that's been modified")
        sel.click("save_button")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("NSFW Enterprises, LLC - Goods Services", sel.get_title())
        self.assertEqual("test good 2", sel.get_table("//div[@id='content']/div/table[1].1.0"))
        sel.click("link=test good 2")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("test good 2", sel.get_value("id_name"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("2000-01-02", sel.get_value("id_introduction_date"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("2020-01-02", sel.get_value("id_sales_discontinuation_date"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("2021-01-02", sel.get_value("id_support_discontinuation_date"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("This is a comment that's been modified", sel.get_value("id_comment"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
