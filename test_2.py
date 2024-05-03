from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def download_pages_with_query(query):
    query = query.lower().replace(' ', '_')
    base_url = 'https://avito.ru'

    # # Опции для браузера
    # chrome_options = Options()
    # chrome_options.add_argument('--headless') # Отключение визуального режима браузера
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')

    # Инициализация браузера
    driver = webdriver.Chrome('chromedriver_linux64/chromedriver')
    # driver.implicitly_wait(10) # Ожидание до 10 секунд для поиска элементов

    # Открытие главной страницы сайта
    driver.get(base_url)


download_pages_with_query('jopa')



#     # Поиск поля ввода
#     search_input = driver.find_element(By.XPATH, "//input[@id='search']")

#     # Ввод запроса пользователя
#     search_input.send_keys(query)
#     search_input.submit()

#     # Поиск и скачивание всех страниц с запросом пользователя
#     page_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/{}?')]".format(query))
#     for link in page_links:
#         page_url = link.get_attribute('href')
#         driver.get(page_url)
#         # Здесь можно продолжить дальнейшую обработку, сохранение страницы и т.д.

#     # Закрытие браузера
#     driver.quit()

# # Пример использования
# # query = input("Введите текст запроса: ")
# query = 'creality'
# download_pages_with_query(query)
