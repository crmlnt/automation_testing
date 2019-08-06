from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/")

for handle in driver.window_handles:
    driver.switch_to.window


def firstStep():
    elm = driver.find_element_by_link_text("Infinite Scroll")
    elm.click()
    time.sleep(5)

def pageDown():
        scroll = driver.find_element_by_tag_name("html")
        num_page_down = 2
        while num_page_down:
            scroll.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
            num_page_down -= 1 

def pageUp():
    scrollUp = driver.find_element_by_tag_name("html")
    scrollUp.send_keys(Keys.PAGE_UP)

        

    






firstStep()
pageDown()
pageUp()

