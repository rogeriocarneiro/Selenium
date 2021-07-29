from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

def open_browser():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver

def go_to_home_page():
    driver.get('http://demostore.supersqa.com/')

def add_first_item_to_cart(driver):
    first_item_btn = driver.find_element(By.CLASS_NAME,'add_to_cart_button')
    first_item_btn.click()

def go_to_cart_page(driver):
    driver.get('http://demostore.supersqa.com/cart/')

def apply_coupon(driver, coupon_code):
    coupon_field = driver.find_element(By.ID, 'coupon_code')
    coupon_field.send_keys(coupon_code)
    apply_coupon_btn = driver.find_element(By.NAME, 'apply_coupon')
    apply_coupon_btn.click()

def verify_cart_has_item():
    cart_item_class = 'cart_item'
    for i in range(5):
        try:
            driver.find_element(By.CLASS_NAME, cart_item_class).is_displayed()
            break
        except NoSuchElementException:
            time.sleep(5)
            driver.refresh()

def get_displayed_error_message(driver):
    return driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div/div[1]/ul/li')


if __name__ == '__main__':
    driver = open_browser()
    go_to_home_page()
    add_first_item_to_cart(driver)
    go_to_cart_page(driver)
    verify_cart_has_item()
    apply_coupon(driver, 'fakeone')

    err_msg = get_displayed_error_message(driver).text
    exp_msg = 'Coupon "fakeone" does not exist!'

    assert err_msg == exp_msg, f"Erro: {err_msg}"
    print('PASS')

