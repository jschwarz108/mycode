#!/usr/bin/python3

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Firefox()
    driver.get("https://www.dominos.com/en/")
    time.sleep(5)

    elem = driver.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div/a[2]")
    elem.click()
    time.sleep(5)

#Click on Austin, TX, Select Find Store
    elem = driver.find_element(By.XPATH, "//*[@id='City']")
    elem.send_keys("Austin")
    elem = driver.find_element(By.XPATH, "//*[@id='Region']")
    elem.send_keys("TX")
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/main/section/article/div/div[2]/div[2]/form/div/button")
    elem.click()
    time.sleep(5)

#click on Curbside Delivery for Pond Springs Store
    elem = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div/div[2]/div[27]/div[3]/div/div[2]/div[1]/a/span[1]")
    elem.click()
    time.sleep(5)

#click on Speciality Pizza
    elem = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div[2]/div[8]/a[1]/div[2]/h2")
    elem.click()
    time.sleep(5)

    # click on Memphis BBQ Chicken
    elem = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/section/div/div[10]/div/a[1]")
    elem.click()
    time.sleep(5)

    # click on Honolulu Hawaiian-
    elem = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/section/div/div[5]/div/a[2]")
    elem.click()
    time.sleep(5)

    # Customize Honolulu Hawaiian-Customize
    #NYCrust
    elem = driver.find_element(By.XPATH,"/html/body/div[5]/div/section/div/div/ol/li[1]/section/div/div[2]/fieldset[2]/label[3]/span[1]")
    elem.click()
    time.sleep(2)
    #Xtra Robust Inspired Tomato Sauce
    elem = driver.find_element(By.XPATH,"/html/body/div[5]/div/section/div/div/ol/li[3]/section/div/div[3]/div[1]/div/label[3]")
    elem.click()
    time.sleep(2)
    #Add to Order
    elem = driver.find_element(By.XPATH,"/html/body/div[5]/div/section/div/div/ol/li[7]/aside/section/div/div[3]/button")
    elem.click()
    time.sleep(3)
    #Cheese it up... no
    elem = driver.find_element(By.XPATH,"/html/body/div[5]/div/section/div/div/div/div/button[1]")
    elem.click()
    time.sleep(3)

    #Checkout
    elem = driver.find_element(By.XPATH,"//*[@id='pageModal']")
    elem.click()
    time.sleep(3)

    #No Additions to the order
    elem = driver.find_element(By.XPATH,"html/body/div[25]/section/div/div/div/button")
    elem.click()
    time.sleep(3)

    #Click Checkout
    elem = driver.find_element(By.XPATH,"/html/body/header/nav[1]/div[1]/div[4]/a")
    elem.click()
    time.sleep(3)
    #Click Checkout
    elem = driver.find_element(By.XPATH,"/html/body/div[5]/div/div[3]/div[2]/button[2]")
    elem.click()
    time.sleep(3)
    #No Extras
    elem = driver.find_element(By.XPATH,"/html/body/div[5]/div/div[3]/div[2]/button[2]")
    elem.click()
    time.sleep(7)
main()
