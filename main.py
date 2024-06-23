from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


# Perform scraping tasks using Selenium
def get_driver():
    # Options to make browsing easier
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('disable-info-bars')
    options.add_argument('start-maximized')
    options.add_argument(
        'disable-dev-shm-usage')
    options.add_argument(
        'no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get('https://titan22.com/')
    return driver


def main():
    driver = get_driver()
    sleep(2)
    driver.find_element(by='xpath', value='//*[@id="shopify-section-header"]/div[1]/div/div[3]/a[2]').click()
    sleep(2)
    driver.find_element(by='id', value='CustomerEmail').send_keys('brunoemelife@gmail.com')
    sleep(2)
    driver.find_element(by='id', value='CustomerPassword').send_keys('bD5@AHQhY8-9zze' + Keys.RETURN)
    sleep(2)
    driver.find_element(by='xpath', value='//*[@id="shopify-section-footer"]/se').click()
    sleep(2)
    driver.close()


main()
