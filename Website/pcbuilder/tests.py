from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# Create your tests here.
class testCases(TestCase):

	# Test of de homepagina correct wordt geladen
	def test(self):
		driver = webdriver.Firefox
		driver.get('http://127.0.01:8000/')
		driver.quit()
		
	'''def test2(self):
		driver = webdriver.Firefox()
		driver.get('http://127.0.01:8000/')
		driver.find_element_by_id("processoren-test-id").click()
		driver.quit()

	#filter op direct leverbaar
	def test3(self):
		driver = webdriver.Firefox()
		driver.get('http://127.0.0.1:8000/processoren')
		driver.find_element_by_id("stockCheck").click()
		driver.quit()

	#klik op eerste in de eerte in de lijst
	def test4(self):
		driver = webdriver.Firefox()
		driver.get('http://127.0.0.1:8000/processoren')
		driver.find_elements_by_xpath("//*[@id='list']/div[1]/div/div[2]/div[2]/a")[0].click()
		driver.quit()

	# selecteer het product
	def test5(self):
		driver = webdriver.Firefox()
		driver.get('http://127.0.0.1:8000/processoren')
		driver.find_elements_by_xpath("//*[@id='list']/div[1]/div/div[2]/div[2]/a")[0].click()
		driver.find_element_by_class_name("selectproduct").click()
		driver.quit()

	#go home
	def test6(self):
		driver = webdriver.Firefox()
		driver.get('http://127.0.0.1:8000/processoren')
		driver.find_elements_by_xpath("//*[@id='list']/div[1]/div/div[2]/div[2]/a")[0].click()
		driver.find_element_by_class_name("selectproduct").click()
		driver.find_elements_by_xpath("/html/body/nav/div/div[1]/a")[0].click()
		driver.quit()

	#sorteer op a-z leverbaar
	def test7(self):
		driver = webdriver.Firefox()
		driver.get('http://127.0.0.1:8000/processoren')
		driver.find_element_by_xpath("//select[@id='sort-by']/option[@value='titel-op']").click()
		driver.quit()
	
	#search
	def test8(self):
		driver = webdriver.Firefox()
		driver.get('http://127.0.01:8000/search')
		driver.find_element_by_id("search").send_keys('intel')
		driver.find_element_by_id("search").send_keys(Keys.ENTER)
		driver.quit()
	
	#pijs filteren
	def test9(self):
		driver = webdriver.Firefox()
		driver.get('http://127.0.0.1:8000/processoren')
		driver.find_element_by_id("sliderMinValue").send_keys('500')
		driver.find_element_by_id("sliderMinValue").send_keys(Keys.ENTER)

		driver.find_element_by_id("sliderMaxValue").send_keys('800')
		driver.find_element_by_id("sliderMaxValue").send_keys(Keys.ENTER)
		driver.quit()

	#contact form
	def test10(self):
		driver = webdriver.Firefox()
		driver.get('http://127.0.0.1:8000/contact')
		driver.find_element_by_id("inputName").send_keys('test')
		driver.find_element_by_id("inputEmail").send_keys('test')
		driver.find_element_by_id("textArea").send_keys('test test')
		driver.find_element_by_id("textArea").submit() 
		driver.quit()'''
		

