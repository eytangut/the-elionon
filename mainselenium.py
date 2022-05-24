from selenium import webdriver
import time
driver = webdriver.Chrome('c:\python\Agmon\webdriver\chromedriver.exe')
driver.get('https://www.court.gov.il/ngcs.web.site/homepage.aspx')
time.sleep(1)
date = driver.find_element_by_xpath('//*[@id="Header1_CaseLocatorHeaderUC2_BamaMonthYearTextBoxHT"]')
date.send_keys('0322')
num = driver.find_element_by_xpath('//*[@id="Header1_CaseLocatorHeaderUC2_BamaCaseNumberTextBoxHT"]')
num.send_keys('8880')
bbutton = driver.find_element_by_xpath('//*[@id="Header1_CaseLocatorHeaderUC2_SearchHeaderCaseButton"]')
bbutton.click()