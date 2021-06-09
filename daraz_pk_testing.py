from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
#driver.get("https://www.daraz.pk/") #front page
#driver.get("https://member.daraz.pk/user/register?spm=a2a0e.login_signup.header.d6.46cc7d68SvNZdo") # Undo this line, this is direct signup page

time.sleep(5)
driver.get("https://www.daraz.pk/smartphones/apple/?page=1&sort=pricedesc&spm=a2a0e.home.cate_1_1.2.7f814937DINRnb&style=list")
time.sleep(5)

#scrolling to the Warranty Type section, using pixels
driver.execute_script("window.scrollBy(0, 1600)","")
time.sleep(20)

'''
print(driver.title) #get title
time.sleep(3)
driver.find_element_by_xpath("//*[@id='anonSignup']/a").click() #click sign up page
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[1]/input").send_keys("12345678910")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div[1]/input").send_keys("Adi")
time.sleep(3)
silder = driver.find_element_by_id("nc_2_n1z")
time.sleep(3)
act = ActionChains(driver)
act.drag_and_drop_by_offset(silder, 342,0)
act.perform()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[8]/div/div/div[3]/button").click() #click okay
time.sleep(3)
#checking password is avalible
pwds_element = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[3]/input")
print(pwds_element.is_displayed())
print(pwds_element.is_enabled())
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div[3]/button").click() #signup button
'''


time.sleep(9)
driver.quit()