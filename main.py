from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
import random

# Geckodriver yolu
gecko_path = r'your/path'  # Geckodriver'ın tam yolunu yazın

# Firefox için webdriver'ı başlat
service = Service(gecko_path)
driver = webdriver.Firefox(service=service)

try:
    while True:
        # Web sitesine git
        driver.get('https://github.com/Lunixizm/')

        # Sayfayı yenile
        driver.refresh()

        # 10 ile 15 saniye arasında random bekle
        wait_time = random.uniform(10, 15)
        time.sleep(wait_time)

except KeyboardInterrupt:
    print("Program sonlandırıldı.")
finally:
    driver.quit()
