from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "/Users/user/Documents/learning/python/kindergarten/chromedriver"


def get_data():
    service = Service(CHROME_DRIVER_PATH)
    browser = webdriver.Chrome(service=service)

    kindergartens = [
        "https://indigo-nursultan.e-orda.kz/ru/view/30185",
        "https://indigo-nursultan.e-orda.kz/ru/view/20094",
    ]

    free_spots_int = 0
    for kindergarten in kindergartens:
        browser.get(kindergarten)
        target_element = browser.find_elements(By.CSS_SELECTOR, ".gn-d-info")
        free_spots_int += 0 if target_element[2].text == 'Общего доступа: 0' else 1
        print(browser.current_url)

    browser.close()
    return free_spots_int
