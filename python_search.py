'''
Because python does not compile I feel like a README file is moot. You can see what the code is doing right here! Of course, I'll add a brief explaination here.

This program loads the "I need a clan" section of the Clash of Clans' forum. It then logs you in and systematically replies to every post on the forum with a given message and title. I've included a basic example message.

Note: you need to enter your user name and password into the code, not at runtime.  
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass
from selenium.common.exceptions import NoSuchElementException

title = "Omnibellum wants YOU!"
	
message = """Level 7 ADULT (18+) Warring clan with experienced players, for now, topping out at TH9. We strive to win every war possible in our quest to level 10. 

Why we are different from others?

We recruit veteran players as well as beginners. While we want to win every war and continue to improve ourselves, our biggest goal is achieving consistency. 

About Us.

Long Tenured clan with very active leadership.

Constant warring tendencies, while searching for our best war size with the players we have in our ranks.

With 20-25 veterans in our ranks we allow our gates to open about once every 4-5 wars to allow new players to come join and find a home with us.

Our top players stay with donation numbers in the thousands, so you will scarcely be short of Clan Castle troops. This includes max leveled wizards, balloons, P.E.K.K.A., etc...

We have a very strong leadership group in close contact with one another constantly improving the environment for the players within the group.

With almost everybody active and constantly improving themselves, we have many players that offer advice and pointers to any question you could possibly need answered. We are here for you.

We are very open to a clan merge if given the opportunity. Adequate ranks will be given to the leadership from the clan in talks.

Clan Tag: #BU2JLUPJ

Clan Rules.

1. We provide a friendly gaming environment for all players. Racism, sexism, or hate speech/attacking of any sort will not be tolerated.

2. We ask our members to keep up with a certain level of activity. You will be required to use both attacks in war. Not doing so will result in removal from the clan.

3. While we always promote helping with donations, and this does help show activity, we do not require any certain number of donation.

4. WE DO NOT ASSIGN WAR ATTACKS. All we ask is that you take careful consideration into who you choose to attack and make a smart, 3-starred attack. If you attack for looting purposes, you will be removed.

5. While we enjoy a multicultural environment, we do require use of the English language only. Communication is extremely important and if you cannot comply you risk harming the structure of war and other operations, and will be removed (not warned).

Promotions.

Promotions are earned through activity (In war and chat), performance, and all decisions will go through co-leader vote. If you ask for promotion, you will not receive one. Demotions follow the same process. Only co-leaders may nominate someone for promotion and this will be done in a co-leader only chat.


Requirements for Admission.

1. 1100 trophy count

2. At least a level 7 TH. We ask that you have your troops levelled to a par but will work with you if your are in the midst of upgrading. We are pretty understanding on this.
3. Stay Active and Communicate."""

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
				time.sleep(2)
				elem.send_keys(Keys.CONTROL + Keys.RETURN)
				driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
				driver.switch_to_window(main_window)
				if SafeToPost() == True:
					writemsg()
				else:  
					driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
					driver.switch_to_window(main_window)	
			else:
				print "Element not found and the exception did not get thrown. Please email the developer with the error in the body of your message"
	except NoSuchElementException:
		driver.find_element_by_xpath('//a[img/@src="http://supercell-forum-content.s3.amazonaws.com/assets/images/pagination/next-right.png"]').click()
