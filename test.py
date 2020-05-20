import time
import math
from selenium import webdriver
import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome(r'E:\Downloads\chromedriver.exe')

def answer_from_alert():
    answer = browser.switch_to.alert.text
    addToClipBoard = answer.split(': ')[-1]
    print('Ответ для stepik.org', addToClipBoard)
    browser.switch_to.alert.accept()

def get_attribute():
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    print(x)
    browser.find_element_by_id('answer').send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_css_selector("[value='robots']").click()
    browser.find_element_by_xpath('//button').click()
    print(browser.switch_to.alert.text)
    browser.quit()

def execute_script():
    #https://stepik.org/lesson/228249/step/6?unit=200781
    browser.get("http://SunInJuly.github.io/execute_script.html")
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(str(math.log(abs(12*math.sin(int(x))))))
    for selector in ('#robotCheckbox', '#robotsRule', '.btn'):
        a = browser.find_element_by_css_selector(selector)
        browser.execute_script("return arguments[0].scrollIntoView(true);", a)
        a.click()
    answer_from_alert()


def file_input():
    #https://stepik.org/lesson/228249/step/8?thread=solutions&unit=200781
    browser.get('http://suninjuly.github.io/file_input.html')
    for selector in browser.find_elements_by_css_selector('.form-group input'):
        selector.send_keys('prprpr')
    element = browser.find_element_by_css_selector('#file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.py')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    browser.find_element_by_css_selector('.btn').click()
    answer_from_alert()


def alert_accept():
    #https://stepik.org/lesson/184253/step/4?unit=158843
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element_by_css_selector(".btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(str(math.log(abs(12*math.sin(int(x))))))
    browser.find_element_by_css_selector(".btn").click()
    time.sleep(1)
    answer_from_alert()

def redirect_accept():
    #https://stepik.org/lesson/184253/step/6?unit=158843
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element_by_css_selector(".btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    browser.find_element_by_css_selector(".btn").click()
    time.sleep(3)
    answer_from_alert()

def explicit_wait2():
    #https://stepik.org/lesson/181384/step/8?unit=156009
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btn = browser.find_element_by_id("book")
    btn.click()
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    a = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", a)
    a.click()
    time.sleep(5)
    answer_from_alert()
    time.sleep(5)



if __name__ == '__main__':
    try:
        s = 'My Na1me is Julia'

        if 'Name' in s:
            print('Substring found')

        index = s.find('Name')
        if index != -1:
            print(f'Substring found at index {index}')
    finally:
        browser.close()
        browser.quit()



