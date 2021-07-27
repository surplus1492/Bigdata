from selenium import webdriver

browser=webdriver.Chrome('./chromedriver.exe')

browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

trs=browser.find_elements_by_css_selector('#weather_table > tbody >tr')

for tr in trs:
    local=tr.find_element_by_css_selector('td:nth-child(1) > a').text
    temp=tr.find_element_by_css_selector('td:nth-child(6)').text

    print('{}, {}'.format(local,temp))

browser.close()