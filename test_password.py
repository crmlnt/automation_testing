from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest

driver = webdriver.Firefox()
driver.get("http://www.the-internet.herokuapp.com")

for handle in driver.window_handles:
    driver.switch_to.window


def test_one():
        elm = driver.find_element_by_link_text("Form Authentication")
        elm.click()

def test_two():
        text = driver.find_element_by_xpath("//*[@id='username']")
        text.send_keys("tomsmith")
        psw = driver.find_element_by_xpath("//*[@id='password']")
        psw.send_keys("SuperSecretPassword!")
        send = driver.find_element_by_xpath("//*[@id='login']/button")
        send.click()
        time.sleep(4)
        sendback = driver.find_element_by_xpath("/html/body/div[2]/div/div/a")
        sendback.click()

test_one()
test_two()

