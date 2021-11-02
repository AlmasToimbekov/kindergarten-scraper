from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER_PATH = "/Users/user/Documents/learning/python/kindergarten/chromedriver"


def get_data():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)

    kindergartens = [
        "https://indigo-nursultan.e-orda.kz/ru/view/30185",
        "https://indigo-nursultan.e-orda.kz/ru/view/20094",
        "https://indigo-nursultan.e-orda.kz/ru/view/40267",
    ]

    free_spots_int = 0
    for kindergarten in kindergartens:
        browser.get(kindergarten)

        all_elements = browser.find_elements(By.CSS_SELECTOR, ".gn-inner")
        target_element = None
        for elem in all_elements:
            if 'от 3' in elem.find_element(By.CSS_SELECTOR, ".gn-d-name").text:
                target_element = elem
                break
        if target_element is None:
            print('No target element found')
            raise ValueError('A very specific bad thing happened.')

        target_element = target_element.find_element(By.CSS_SELECTOR, ".gn-d-info")
        free_spots_int += 0 if target_element.text == 'Общего доступа: 0' else 1
        print(browser.current_url, free_spots_int)

    browser.close()
    return free_spots_int
