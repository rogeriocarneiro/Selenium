from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#importing the python debugger
import pdb


driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')

# By.ID examples - more stable option
cart = driver.find_element(By.ID, "site-header-cart")
cart_text = cart.text
print(f'{cart.text} \n {type(cart)}')

search_field = driver.find_element(By.ID, "woocommerce-product-search-field-0")
search_field.send_keys('Hoodie')
# search_field.send_keys(Keys.ENTER)

# By.CSS_SELECTOR
# examples - best option when there is no id related directly to the item
# my_acct = driver.find_element(By.XPATH,
#                               '//*[@id="site-navigation"]/div[1]/ul/li[4]')
# my_acct.click()


pdb.set_trace()
# in the debugger this line of code creates, you can use the command dir(~)
# to list all the methods accepted by the instance u've created (e.g. search_box or driver).


# quit will finish all browser sections oppened
# driver.quit()
# close will finish just the current browser section
# fdriver.close()
