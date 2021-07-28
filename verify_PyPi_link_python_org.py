from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get('https://www.python.org/')

pypi_header_link_locator = '#top > nav > ul > li.pypi-meta > a'
pypi_header_link_elm = driver.find_element(By.CSS_SELECTOR, pypi_header_link_locator)
pypi_header_link_elm.click()

cur_title = driver.title
expected_title = "PyPI · The Python Package Index"
# if cur_title != expected_title:
#     raise Exception('sei não hem')

cur_url = driver.current_url
expected_url = 'https://pypi.org/'
assert cur_url == expected_url, f'Clicked on Pypi but the url opened was {cur_url}'
print("PASS")

driver.quit()