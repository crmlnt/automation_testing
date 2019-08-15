from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import pytest


driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

for handle in driver.window_handles:
    driver.switch_to.window

def test_findLink():
    elm = driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[31]/a")
    elm.click()
    time.sleep(2)

def test_keyPress():
    keyOne = driver.find_element_by_xpath("//*[@id='target']")
    keyOne.send_keys("H")
    assert driver.page_source.find("H")
    time.sleep(1)            
    keyTwo = driver.find_element_by_xpath("//*[@id='target']")
    keyTwo.send_keys("E")
    assert driver.page_source.find("E")
    time.sleep(1)
    keyThree = driver.find_element_by_xpath("//*[@id='target']")
    keyThree.send_keys("Y")
    assert driver.page_source.find("Y")
    time.sleep(1)
    keyFour = driver.find_element_by_xpath("//*[@id='target']")
    keyFour.send_keys("!")
    assert driver.page_source.find("!")




