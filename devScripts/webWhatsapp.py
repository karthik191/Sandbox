from selenium import webdriver
import time
#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
#driver.get('https://web.whatsapp.com/')

name = 'Sas shivananda'
filepath = 'D:\est_image.jpg'

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
attachment_box.click()

image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

time.sleep(3)

send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
send_button.click()