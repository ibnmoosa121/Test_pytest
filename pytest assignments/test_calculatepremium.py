from selenium import webdriver
#from selenium.webdriver.remote import webelement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select





driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()


driver.get("http://demo.guru99.com/insurance/v1/index.php")
driver.find_element_by_id("email").send_keys("mohammedkhurram14@gmail.com")
driver.find_element_by_id("password").send_keys("123")
driver.find_element_by_name("submit").click()

#quotation request
driver.find_element_by_id("ui-id-2").click() 
driver.find_element_by_id("quotation_windscreenrepair_t").click()
driver.find_element_by_id("quotation_incidents").send_keys("accident hogaya")
driver.find_element_by_id("quotation_vehicle_attributes_registration").send_keys("1234")
driver.find_element_by_id("quotation_vehicle_attributes_mileage").send_keys("40kmph")
driver.find_element_by_id("quotation_vehicle_attributes_value").send_keys("1000")

element = driver.find_elements_by_id("quotation_vehicle_attributes_policystart_2i")
drp = Select (element)

#drp.select_by_index(2)
drp.select_by_visible_text('Driveway/Carport')
#drp.select_by_value('Driveway')

driver.find_element_by_xpath('//*[@id="new_quotation"]/div[8]/input[1]').click()
driver.find_element_by_id('resetquote').click()















 

