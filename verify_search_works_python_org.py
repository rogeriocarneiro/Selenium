from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get('https://www.python.org/')

cur_title = driver.title
expected_title = "Welcome to Python.org"
if cur_title != expected_title:
     raise Exception('sei não hem')


search_field_id = '#id-search-field'
search_field_elm = driver.find_element(By.CSS_SELECTOR, search_field_id)
search_field_elm.send_keys('testing')

go_btn_id = 'submit'
go_btn_elm = driver.find_element(By.ID, go_btn_id)
go_btn_elm.click()

first_result_xpath = '//*[@id="content"]/div/section/form/ul/li[1]'
first_result_elm = driver.find_element(By.XPATH, first_result_xpath)
#import pdb; pdb.set_trace()
if first_result_elm.is_displayed():
    print('PASS')
else:
    print(f"After searching, the result wasn't displayed.")

driver.quit()