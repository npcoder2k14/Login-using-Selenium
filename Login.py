from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.PhantomJS()
driver.set_window_size(1120,550)

driver.get("http:10.10.2.1")
#time.sleep(5)
res=0
try:
    e1=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.NAME,"username"))
    )
    e2=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.NAME,"passwd"))
    )
    e3=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.LINK_TEXT,"Login"))
    )
    driver.find_element_by_name('username').send_keys('narendra')
    driver.find_element_by_name('passwd').send_keys('Banda123')
    driver.find_element_by_name('rememberme').click()
    #res=e1&e2&e3
    res=BeautifulSoup(driver.page_source)
    if "Connected(Default Internet)" not in res.text :
        driver.find_element_by_css_selector('.field2 input').click()
    #print(res)
    res=1
    #time.sleep(5)
#a=driver.find_element_by_css_selector('.field2'(1))
#print(a)
    #print(driver.current_url)
finally:
    if res :
        print("Successful!!")
        time.sleep(5)
    else:
        print("Failed :(")
driver.quit()
