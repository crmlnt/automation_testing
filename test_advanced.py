from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
import time
import pytest


driver = webdriver.Firefox()
driver.get("http://automationpractice.com/index.php")
time.sleep(3)

for handle in driver.window_handles:
    driver.switch_to.window



def firstScenario():
        cart = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div[1]/ul[1]/li[1]/div/div[1]/div/a[1]/img")
        cart.click()
        time.sleep(2)
        cartButton = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[3]/div[1]/p/button")
        cartButton.click()
        time.sleep(5)
        driver.back()
        time.sleep(3)
        cartPage = driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[3]/div/a")
        cartPage.click()
        deleteButton = driver.find_element_by_id("1_1_0_0")
        deleteButton.click()
        assert driver.page_source.find("Your shopping cart is empty")


firstScenario()

