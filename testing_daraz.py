from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import logging

#path of Chrome wweb driver
driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")

#logs are saved to file for easy read
logging.basicConfig(filename="C://Users//addyf//Desktop//Certificates//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s,',
                    datefmt='%m/%d/%y: %I: %M: %S %p ',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#miximize the window
driver.maximize_window()
time.sleep(2)
logger.info("Browser Window is maximized")

#Opening daraz.pk website
driver.get("https://www.daraz.pk/")
time.sleep(2)
logger.info("Website is opened")

#Verifying the title name
assert "Online Shopping in Pakistan: Fashion, Electronics & Books - Daraz.pk" in driver.title  #conform


cookies = driver.get_cookies() #Capture all the cookies created by browser
print(len(cookies))  #print number of cookies have been created
print(cookies) #print all the cookies pairs

#mouse hover actions to navigate
devices = driver.find_element_by_xpath('//*[@id="Level_1_Category_No1"]/a/span')
time.sleep(2)
mobile = driver.find_element_by_xpath('//*[@id="J_5022174600"]/div/ul/ul[1]/li[1]/a/span')
time.sleep(2)
iphone = driver.find_element_by_xpath('//*[@id="J_5022174600"]/div/ul/ul[1]/li[1]/ul/li[2]/a/span')
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(devices).move_to_element(mobile).move_to_element(iphone).click().perform()
time.sleep(4)

#undo this line, its is a direct link to iphone page
#driver.get("https://www.daraz.pk/smartphones/apple/?spm=a2a0e.home.cate_1_1.2.66294937SnuF7j&style=list")
time.sleep(2)
#another way of view all items, individual items
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[4]/span[2]/i").click()
time.sleep(5)
#scrolling to a specific item
flag = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[3]/div[7]/div/div[2]/div[2]/a")
driver.execute_script("arguments[0].scrollIntoView();",flag)
time.sleep(9)
#selecting an item
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[3]/div[8]/div/div[1]/div/div[1]/a/img").click()
time.sleep(2)

driver.save_screenshot("C:/Users/addyf/Desktop/Certificates/selected_item_img.png")


#undo this line, its is a direct link to the selected item
#driver.get("https://www.daraz.pk/products/iphone-12-pro-max-6gb-ram-1-year-official-warranty-pta-approved-i196760114-s1392034668.html?")
time.sleep(2)

#mouse actions to CHANGE COLOURS of selected item
for i in range(1,5):
    color = driver.find_element_by_xpath(f'/html/body/div[4]/div/div[2]/div[2]/div/div[1]/div[12]/div/div[1]/div/div/div[2]/span[{i}]')
    time.sleep(2)

    actions = ActionChains(driver)
    actions.move_to_element(color).perform()
    time.sleep(2)

#click on ADD TO CART
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div/div[1]/div[15]/div/button[2]/span/span").click()
time.sleep(2)
#back to items page because login frames are not there
driver.back()
#forward to selected item
driver.forward()

#scrolling to the comments section, using pixels
driver.execute_script("window.scrollBy(0,2700)","")
for i in range(1,6):
    driver.find_element_by_xpath(f"/html/body/div[4]/div/div[8]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/div/button[{i}]").click()
    time.sleep(4)

driver.back()

'''#scrolling to the comments section, using xpath
flag = driver.find_element_by_xpath("/html/body/div[4]/div/div[8]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/button[1]/i")
driver.execute_script("arguments[0].scrollIntoView();",flag)
time.sleep(5)
'''

#scrolling to the color family section, using pixels
driver.execute_script("window.scrollBy(0,-1000)","")

#driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[11]/div[2]/div/div/label[1]/span[2]").click()

#first check if radio box is selected brand
result = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[11]/div[2]/div/div/label[1]/span[2]').is_selected()
if result:
    print('Checkbox already selected')
else:
    driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[11]/div[2]/div/div/label[1]/span[2]').click()
    print("Checkbox selected")
time.sleep(5)

#Search for bags
driver.find_element_by_id("q").send_keys("bags")
time.sleep(1)
driver.find_element_by_id("q").send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element_by_xpath("//*[@id='anonSignup']/a").click() #click sign up page
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[1]/input").send_keys("12345678910")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div[1]/input").send_keys("Adi")
time.sleep(1)
silder = driver.find_element_by_id("nc_2_n1z")

act = ActionChains(driver)
act.drag_and_drop_by_offset(silder, 342,0)
act.perform()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[8]/div/div/div[3]/button").click() #click okay

#checking password is avalible
pwds_element = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[3]/input")
print(pwds_element.is_displayed())
print(pwds_element.is_enabled())

driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div[3]/button").click() #signup button



time.sleep(9)
#driver.quit()