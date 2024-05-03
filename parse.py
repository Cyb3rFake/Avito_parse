from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType


# prox = Proxy()
# prox.proxy_type = ProxyType.MANUAL
# prox.http_proxy = "ip_addr:port"
# prox.socks_proxy = "ip_addr:port"
# prox.ssl_proxy = "ip_addr:port"

# capabilities = webdriver.DesiredCapabilities.CHROME
# prox.add_to_capabilities(capabilities)

# driver = webdriver.Chrome(desired_capabilities=capabilities)




# Получаем текст запроса от пользователя
# search_query = input("Введите текст запроса: ")
search_query = "дом"

# Запускаем веб-драйвер (Chrome)
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only

chrome_options.add_argument("--headless=new") # for Chrome >= 109
chrome_options.add_argument("--headless")
chrome_options.headless = True # also works


driver = webdriver.Chrome(options=chrome_options)

region = "all"


# driver.get("file:///media/hdd0/Python_Projects/Avito_parser/tst_page/page1.html")

# Переходим на страницу поиска
driver.delete_all_cookies()
driver.get(f"https://www.avito.ru/{region}?p=1&q={search_query}")



def get_data(elements):

    for num,el in enumerate(elements[::],1):
        
        id = el.get_attribute("id")
        title = el.find_element(By.XPATH,f'//*[@id="{id}"]/div/div/div[2]/div[2]/div/a/h3').text
        price = el.find_element(By.TAG_NAME,"p").text
        description = el.find_element(By.CSS_SELECTOR,"[class^='iva-item-descriptionStep-']").text
        geo = el.find_element(By.CSS_SELECTOR,"[class^='geo-root-']").text
        link = el.find_element(By.XPATH, f'//*[@id="{id}"]/div/div/div[2]/div[2]/div/a').get_attribute('href')
        
        #print(num)
        print("Заголовок:", title)
        print("Описание:", description)
        print("Цена:", price)
        print("Ссылка:", link)
        print("Адрес:", geo)
        print("\n")
            



# //*[@id="app"]/div/div[4]/div/div[2]/div[3]/div[3]/div[4]/div/div/a[11]

# Ждем загрузки результатов поиска
# results_loaded = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "items-items-kAJAg"))
# )
results_loaded = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div/div[2]/div[3]/div[3]/div[4]'))
)


# Получаем все блоки с объявлениями
items = driver.find_element(By.CLASS_NAME, 'items-items-kAJAg')
# items = driver.find_element(By.CSS_SELECTOR, "[class^='items-items-']")
elements = items.find_elements(By.CSS_SELECTOR,"[id^='i']")



# Получаем колличество страниц

# last_page_link = [l.get_attribute("href") for l in driver.find_element(By.CSS_SELECTOR, '#app > div > div.styles-singlePageWrapper-eKDyt > div > div.index-center-_TsYY.index-center_withTitle-_S7ge.index-centerWide-_7ZZ_.index-center_marginTop_1-ewXHO > div.index-inner-dqBR5.index-innerCatalog-ujLwf > div.index-content-_KxNP > div.js-pages.pagination-pagination-_FSNE > div > div').find_elements(By.TAG_NAME, 'a')][-1]
# last_page_num = last_page_link[last_page_link.find("=")+1:last_page_link.find("&")]

# pages_count = items.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[2]/div[3]/div[3]/div[4]').text.splitlines()[-1]

last_page_link = items.find_element(By.XPATH, "//a[@class='pagination-page'][last()]").get_attribute('href')
last_page_num = last_page_link[last_page_link.find("=")+1:last_page_link.find("&")]


print(last_page_num)






# print(elements[4].find_element(By.XPATH, '//*[@id="i3918654554"]/div/div/div[2]/div[2]/div/a').get_attribute('href'))
# print(elements[4].find_element(By.CSS_SELECTOR,"[class^='iva-item-title-']").find_element(By.TAG_NAME, 'a').find_element(By.TAG_NAME, 'h3').get_attribute('gref'))

# print(elements[4].find_element(By.CSS_SELECTOR,"[class^='iva-item-descriptionStep-']").text)
# print(elements[4].find_element(By.CSS_SELECTOR,"[class^='iva-item-title-']").text)
# print(elements[4].find_element(By.CSS_SELECTOR,"[class^='geo-root-']").text)

# print(elements[4].find_element(By.CSS_SELECTOR,"").text)










driver.quit()

# --------


# # Проходим по каждому объявлению
# for item in items:
#     # Получаем заголовок, цену и ссылку для каждого объявления
#     title = item.find_element_by_class_name("snippet-link").text
#     price = item.find_element_by_class_name("snippet-price").text
#     link = item.find_element_by_class_name("snippet-link").get_attribute("href")

#     # Выводим результаты
#     print("Заголовок:", title)
#     print("Цена:", price)
#     print("Ссылка:", link)
#     print("\n")

# # Переходим на следующие страницы поиска
# next_page = driver.find_element_by_class_name("pagination-next")
# while next_page.is_enabled():
#     next_page.click()
#     items = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.CLASS_NAME, "item"))
#     )

#     for item in items:
#         title = item.find_element_by_class_name("snippet-link").text
#         price = item.find_element_by_class_name("snippet-price").text
#         link = item.find_element_by_class_name("snippet-link").get_attribute("href")

#         print("Заголовок:", title)
#         print("Цена:", price)
#         print("Ссылка:", link)
#         print("\n")

#     next_page = driver.find_element_by_class_name("pagination-next")

# # Завершаем работу скрипта
# driver.quit()

