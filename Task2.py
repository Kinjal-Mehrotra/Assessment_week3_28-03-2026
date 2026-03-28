## Task 2
### Vogue.in automation using python selenium
#1. Navigate to https://www.vogue.in/
# 2. Click on `Shopping` category
# 3. Scroll to `Olive Crest (Wings)` product and click on it
# 4. New tab opens switch to the new window
# 5. Fetch me the {name:price}

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

#navigating to the website
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.vogue.in/')
driver.maximize_window()

#creating wait object
wait=WebDriverWait(driver,5)

#going to shopping category
wait.until(ec.visibility_of_element_located((By.XPATH,'//a[text()="Shopping"]'))).click()

#finding the product
olive_crest_product=wait.until(ec.presence_of_element_located((By.XPATH,"(//a[contains(@data-offer-url,'olive')])[3]")))
action=ActionChains(driver)
action.move_to_element(olive_crest_product).perform()
olive_crest_product.click()

#switching to the product window
all_windows=driver.window_handles
driver.switch_to.window(all_windows[-1])

#getting the product details
product_name=wait.until(ec.presence_of_element_located((By.XPATH,'//h1[@class="product-title title mb-0 h2"]')))
print("Product name: ", product_name.text)
product_price=wait.until(ec.presence_of_element_located((By.XPATH,'//span[@class="money buckscc-money"]')))
print("Product price: ", product_price.text)

sleep(5)
driver.quit()
