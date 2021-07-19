from selenium import webdriver



def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_login():
    driver.get("http://demo.guru99.com/insurance/v1/index.php")
    driver.find_element_by_id("email").send_keys("mohammedkhurram14@gmail.com")
    driver.find_element_by_id("password").send_keys("123")
    driver.find_element_by_name("submit").click()
    x =  driver.title
    assert x == "Insurance Broker System"

