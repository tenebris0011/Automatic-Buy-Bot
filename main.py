# This is a sample Python script.
from bs4 import BeautifulSoup as bs
import requests
import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def scraper():
    url = "https://discuss.python.org/t/help-with-request-get-access-denied/6540"
    req = requests.get(url)
    soup = bs(req.content, 'html.parser')

def automateBestBuy():
    options = webdriver.ChromeOptions()
    # options.headless = True
    driver = webdriver.Chrome(executable_path='C:\\Users\\Nathan\\PycharmProjects\\webscraper\\assets\\chromedriver.exe', options=options)
    driver.maximize_window()
    driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789")
    # driver.get("https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659")

    buyButton = False

    # time.sleep(1)
    sleep = time.sleep(1)

    while not buyButton:
        try:
            time.sleep(1)
            addToCartBtn = addButton = driver.find_element_by_class_name("btn-disabled")

            print("Button isn't ready yet.")

            time.sleep(5)
            driver.refresh()

        except:
            time.sleep(1)
            addToCartBtn = addButton = driver.find_element_by_class_name("btn-primary")

            print("Button was clicked.")
            addToCartBtn.click()
            buyButton = True

            time.sleep(1)
            driver.get("https://www.bestbuy.com/cart")
            checkoutBtn = addButton = driver.find_element_by_class_name("btn-primary")
            checkoutBtn.click()

            time.sleep(2)
            elem = driver.find_element_by_class_name("tb-input ")
            elem.send_keys("email")
            elem2 = driver.find_element_by_id("fld-p1")
            elem2.send_keys("password")

            sgninBtn = addButton = driver.find_element_by_class_name("btn-secondary")
            sgninBtn.click()

            time.sleep(2)
            exitBtn = addButton = driver.find_element_by_class_name("btn-primary")
            exitBtn.click()

            swithBtn = addButton = driver.find_element_by_class_name("ispu-card__switch")
            swithBtn.click()

            plcOrdBtn = addButton = driver.find_element_by_class_name("btn-primary")
            plcOrdBtn.click()

            time.sleep(100000)


    # driver.save_screenshot("test.png")

    # time.sleep(5)
    driver.close()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    automateBestBuy()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
