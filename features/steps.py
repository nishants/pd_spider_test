from lettuce import step
from splinter.browser import Browser
from lettuce import world
import pages 

@step('I am on home page')
def go_to_homepage(step):
    pages.visit_home_page()

@step('I click on add new link')
def click_submit_new(step):
	pass