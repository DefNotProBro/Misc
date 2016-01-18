'''
Because python does not compile I feel like a README file is moot. You can see what the code is doing right here! Of course, I'll add a brief explaination here.

This program loads the "I need a clan" section of the Clash of Clans' forum. It then logs you in and systematically replies to every post on the forum with a given message and title. I've included a basic example message.

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass
from selenium.common.exceptions import NoSuchElementException
from random import randint

title = raw_input("Title: ")
	
message_path = raw_input("Path to message text: ")
with open(message_path) as f:
	message = f.readlines()

def writemsg():
       	driver.find_element_by_id("newreplylink_top").click()
	try:	
       		elem = driver.find_element_by_id("title")
        	elem.send_keys(title)
	except NoSuchElementException:
		driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
		driver.switch_to_window(main_window)
		return
	driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
        elem = driver.find_element_by_class_name("forum")
	time.sleep(5)
        elem.send_keys(message)
	driver.switch_to_default_content() 
        driver.find_element_by_id("vB_Editor_001_save").click()
	driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
	driver.switch_to_window(main_window)

def SafeToPost():
	while True: 
		elems = driver.find_elements_by_class_name("title icon")
		for elem in elems:
			if elem.text == title:
				return False
		try:
			driver.find_element_by_xpath('//a[img/@src="http://supercell-forum-content.s3.amazonaws.com/assets/images/pagination/next-right.png"]').click()
		except NoSuchElementException:
			return True
		return True
	
username = raw_input("Username: ")
password = getpass.getpass('Password: ')

driver = webdriver.Firefox()
driver.get("http://forum.supercell.net/forumdisplay.php/56-I-Need-A-Clan!")
elem = driver.find_element_by_name("vb_login_password_hint")
elem.send_keys(password)
elem = driver.find_element_by_name("vb_login_username")
elem.send_keys(username)
elem.send_keys(Keys.RETURN)
time.sleep(10)
while True:
	try:
		elems = driver.find_elements_by_class_name("title")
		main_window = driver.current_window_handle
		for elem in elems:
			if elem.is_displayed():
				time.sleep(randint(60, 70))
				elem.send_keys(Keys.CONTROL + Keys.RETURN)
				driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
				driver.switch_to_window(main_window)
				writemsg()	
			else:
				print "Element not found and the exception did not get thrown. Please email the developer with the error in the body of your message"
	except NoSuchElementException:
		driver.find_element_by_xpath('//a[img/@src="http://supercell-forum-content.s3.amazonaws.com/assets/images/pagination/next-right.png"]').click()
