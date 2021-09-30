from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver_ = webdriver.Chrome(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = r"C:\Users\Yevhenii Lukianchuk\Downloads\chromedrive.exe"     # insert your path here

inp = ["apple", "banana", "BTC"]    # input queries list


def get_first_picture_link(driver, query):
    driver.get('https://google.com/')
    img_b = driver.find_element_by_xpath("//a[contains(text(),'Images')]")
    img_b.click()
    p = driver.find_element_by_name("q")
    p.send_keys(query)
    p.submit()
    w = WebDriverWait(driver, 5)
    first_picture = driver.find_element_by_xpath("//div[@id='islrg']/div/div/a/div/img")
    first_picture.click()
    side_pic_xpath = "//div[@id='Sva75c']/div/div/div[3]/div[2]/c-wiz/div/div/div/div[2]/div/a/img"
    side_picture = driver.find_element_by_xpath(side_pic_xpath)
    w.until(ec.visibility_of_element_located((By.XPATH, side_pic_xpath)))
    link = side_picture.get_attribute('src')
    # Even after the visibility of the element is located src returns data instead of the link for some time

    counter = 0
    while link[:4] != 'http':
        counter +=1
        link = side_picture.get_attribute('src')
        if counter > 1000:
            return None
    return link


output = {}
for i in inp:
    output[i] = get_first_picture_link(driver_, i)

print(output)

driver_.close()
