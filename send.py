from selenium import webdriver
from selenium.webdriver.chrome import service

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Opera\\53.0.2907.68\\opera.exe"# path to opera executable
driver = webdriver.Opera(options=options)

#driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')
input('Press "Enter" after scanning QR code')

name = input('Enter the name of user or group: ')
msg = input('Message: ')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('_2bXVy')
msg_box.send_keys(msg)
button = driver.find_element_by_class_name('_2lkdt')
button.click()
