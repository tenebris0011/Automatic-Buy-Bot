from selenium import webdriver
import time
from configparser import ConfigParser

global file
file = './assets/config.ini'

def automateBestBuy():
    options = webdriver.ChromeOptions()
    # options.headless = True
    driver = webdriver.Chrome(executable_path='C:\\Users\\Nathan\\PycharmProjects\\webscraper\\assets\\chromedriver.exe', options=options)
    driver.maximize_window()
    driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442")
    # driver.get("https://www.bestbuy.com/site/dynex-5-w-usb-wall-charger-white/6403449.p?skuId=6403449")

    buyButton = False

    while not buyButton:
        try:
            addToCartBtn = addButton = driver.find_element_by_class_name("btn-disabled")

            print("Button isn't ready yet.")

            time.sleep(2)
            driver.refresh()

        except:
            addToCartBtn = addButton = driver.find_element_by_class_name("btn-primary")

            print("Button was clicked.")
            addToCartBtn.click()
            buyButton = True

            time.sleep(2)
            driver.get("https://www.bestbuy.com/cart")

            time.sleep(2)
            checkoutBtn = addButton = driver.find_element_by_class_name("btn-primary")
            checkoutBtn.click()

            time.sleep(2)
            elem = driver.find_element_by_class_name("tb-input ")
            elem.send_keys(account['email'])
            elem2 = driver.find_element_by_id("fld-p1")
            elem2.send_keys(account['password'])

            time.sleep(2)
            sgninBtn = addButton = driver.find_element_by_class_name("btn-secondary")
            sgninBtn.click()

            time.sleep(2)
            exitBtn = addButton = driver.find_element_by_class_name("btn-primary")
            exitBtn.click()

            time.sleep(2)
            swithBtn = addButton = driver.find_element_by_class_name("ispu-card__switch")
            swithBtn.click()

            time.sleep(2)
            btn = addButton = driver.find_element_by_id("credit-card-cvv")
            btn.send_keys(card['cvv'])

            time.sleep(2)
            plcOrdBtn = addButton = driver.find_element_by_class_name("button__fast-track")
            plcOrdBtn.click()

            time.sleep(100000)

    driver.close()

if __name__ == '__main__':
    config = ConfigParser()
    config.read(file)
    account = config['login']
    card = config['card']

    automateBestBuy()
