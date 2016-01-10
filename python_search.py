from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

def writemsg():
        message = "Hello there! You sound perfect for our clan! \r\n\r\nWe are an active war clan seeking members who are able to three-star their opponent in wars! \r\n\r\nWe are a level 7 war clan, and you can find us by searching for \"Omnibellum\""

        title = "Omnibellum wants YOU!"
	
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

username = "username"
password = "password"

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
		time.sleep(65)
		elems = driver.find_elements_by_class_name("title")
		main_window = driver.current_window_handle
		for elem in elems:
			if elem.is_displayed():
				elem.send_keys(Keys.CONTROL + Keys.RETURN)
				driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
				driver.switch_to_window(main_window)
				writemsg()
			else:
				print "Element not found"
	except NoSuchElementException:
		driver.find_element_by_xpath('//a[img/@src="http://supercell-forum-content.s3.amazonaws.com/assets/images/pagination/next-right.png"]').click()
