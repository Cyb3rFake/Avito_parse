from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.avito.ru/moskva/bytovaya_elektronika'
PAUSE_DURATION_SECONDS = 5

chrome_options = Options()
# options.headless = True
chrome_options.add_argument('--headless')
chrome_options.headless = True


def save_html(data):
    if  data:
        with open('index.html', 'wb') as f:
            f.write(data)
    else:
        print("Empty data!")


def main():
    driver.get(URL)
    save_html(driver.page_source.encode("utf-8"))
    
    sleep(PAUSE_DURATION_SECONDS)


if __name__ == '__main__':
    try:
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        main()
    except Exception as e:
        print(e)
    finally:
        driver.quit()
