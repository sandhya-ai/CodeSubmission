from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

browser=webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.maximize_window()
browser.get('https://impl.workday.com/pfizer')
wait = WebDriverWait(browser,5)
browser.find_element_by_id('username').send_keys('KUPPUS05')
browser.find_element_by_id('password').send_keys('2103')
browser.find_element_by_id('submit_button').click()

wait = WebDriverWait(browser,15)
browser.find_element_by_id('password').send_keys('SArath21*()')
browser.find_element_by_id('submit_button').click()






