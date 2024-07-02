import subprocess
import time
import psutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def connect_vpn(config_path):
    # PowerShell command to run OpenVPN with elevated privileges
    powershell_command = (
        f'powershell -Command "Start-Process cmd -ArgumentList \'/k cd /d C:\\Program Files\\OpenVPN\\bin && '
        f'openvpn --config {config_path}\' -Verb RunAs"'
    )
    # Execute the PowerShell command
    process = subprocess.Popen(powershell_command, shell=True)
    return process


def find_openvpn_process():
    time.sleep(5)
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == 'openvpn.exe':
            return process
    return None


def disconnect_vpn(openvpn_process):
    if openvpn_process:
        openvpn_process.terminate()


def get_driver():
    # Options to make browsing easier
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('disable-info-bars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get('https://titan22.com/')
    return driver


def main():
    config_path = "C:\\Users\\Admin\\Downloads\\us-free-177019.protonvpn.udp.ovpn"
    vpn_process = connect_vpn(config_path)

    # Perform web scraping tasks using Selenium
    driver = get_driver()
    time.sleep(2)
    driver.find_element(by='xpath', value='/html/body/header/div[1]/div[1]/div/div[3]/a[2]').click()
    time.sleep(2)
    driver.find_element(by='id', value='CustomerEmail').send_keys('test@email.com')
    time.sleep(2)
    driver.find_element(by='id', value='CustomerPassword').send_keys('*********' + Keys.RETURN)
    time.sleep(10)
    driver.find_element(by='xpath', value='//*[@id="shopify-section-footer"]/se').click()
    time.sleep(2)

    # Find the OpenVPN process
    openvpn_process = find_openvpn_process()

    # Disconnect the VPN
    disconnect_vpn(openvpn_process)

    driver.close()


if __name__ == "__main__":
    main()
