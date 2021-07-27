from selenium import webdriver

browser=webdriver.Chrome('./chromedriver.exe')

browser.get('http://naver.com')

btn_login=browser.find_element_by_css_selector('#account > a')

btn_login.click()

input_id=browser.find_element_by_css_selector('#id')
input_pw=browser.find_element_by_css_selector('#pw')
input_id.send_keys('asdf')
input_pw.send_keys('123456')

btn_submit=browser.find_element_by_css_selector('#log\.login')
btn_submit.click()

browser.close()