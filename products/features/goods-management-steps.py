from lettuce import *
from lettuce.django import django_url
from nose.tools import assert_equals
from selenium import selenium
from tests.pages import *
from django.test.utils import setup_test_environment

@step(r'a logged in user')
def a_logged_in_user( step):
	world.homePage.open()
	world.loginPage.login()
	assert world.homePage.title == world.selenium.get_title(), "Not on home page"


@step('a new good called (.*)')
def a_new_good_called( step, name):
	world.homePage.selectGoodsAndServices()
	world.productsPage.onPage()
	world.productsPage.selectAddGoods();
	world.addGoodPage.onPage()
	world.addGoodPage.enterName( name)

@step(r'the user saves')
def the_user_saves( step ):
	world.addGoodPage.save()

@step(r'then the good should be saved in the database')
def goodIsInTheDatabase( step):
	assert False, "TBI"

@step(r'on the list of goods')
def onListOfGoods( step):
	assert False, "TBI"





@before.all
def before_all():
	print("Setting up database")
	setup_test_environment()

	print("Setting up selenium")
	world.selenium = selenium("localhost", 4444, "*chrome", django_url("/"))
	world.selenium.start()

	print("Setting up pages")
	world.homePage = HomePage( world.selenium)
	world.loginPage = LoginPage( world.selenium)
	world.productsPage = ProductsPage( world.selenium)
	world.addGoodPage = AddGoodPage( world.selenium)
    

@after.all
def after_all(total):
	print("after all")
	world.selenium.stop()
