from selenium import webdriver
from selenium.webdriver.chrome import service

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Opera\\53.0.2907.68\\opera.exe"# path to opera executable
driver = webdriver.Opera(options=options)
driver.implicitly_wait(10)

#driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
input('Press "Enter" after scanning QR code')

#Find Group Name
grps = driver.find_elements_by_xpath('//div[@class = "{}"]/div/span'.format("_25Ooe"))
count = 0
for grp in grps:
	count += 1
	print("Group " + str(count) + ": %s" % grp.get_attribute("title"))

#Find User
usrs = driver.find_elements_by_xpath('//span[@class = "{}"]/span'.format("_2ZEQ2"))
count = 0
for usr in usrs:
	count += 1
	print("User " + str(count) + ": %s" % usr.get_attribute("title"))
	user = driver.find_element_by_xpath('//span[@title = "' + str(usr.get_attribute("title")) + '"]')
	user.click()
	msgs = driver.find_elements_by_xpath('//div[contains(@class,"_3_7SH _3DFk6 message-in")]/div/div/div/span[@class ="selectable-text invisible-space copyable-text"]')
	for msg in msgs:
		print("Message: %s" % msg.get_attribute("innerHTML"))
