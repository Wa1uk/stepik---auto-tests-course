import pytest
from selenium import webdriver
import time



def unit1():
    browser = webdriver.Chrome(r'E:\Downloads\chromedriver.exe')
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)
    browser.find_element_by_xpath("//input[@placeholder='Input your first name']").send_keys('Mihael')
    browser.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys('Jordan')
    browser.find_element_by_xpath("//input[@placeholder='Input your email']").send_keys('Jordan')
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text, "Should be absolute value of a number1"
    browser.quit()

def unit2():
    browser = webdriver.Chrome(r'E:\Downloads\chromedriver.exe')
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)
    browser.find_element_by_xpath("//input[@placeholder='Input your first name']").send_keys('Mihael')
    browser.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys('Jordan')
    browser.find_element_by_xpath("//input[@placeholder='Input your email']").send_keys('Jordan')
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text, "Should be absolute value of a number2"
    browser.quit()

def test_unitest21():
    unit1()


def test_unitest22():
    unit2()

if __name__ == "__main__":
    test_unit1()
    test_unit2()