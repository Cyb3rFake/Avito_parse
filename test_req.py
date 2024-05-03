from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.avito.ru/moskva?q"

# Получаем текст запроса от пользователя
# search_query = input("Введите текст запроса: ")
search_query = "дом"

# Запускаем веб-драйвер (Chrome)
driver = webdriver.Chrome()


region = "all"
# Переходим на страницу поиска
driver.get(f"https://www.avito.ru/{region}?q={search_query}")

# Ждем загрузки результатов поиска
# results_loaded = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "n-snippet-list"))
# )

# Получаем все блоки с объявлениями
items = driver.find_elements_by_class_name("item")
# print(items)
# driver.quit()
# --------


# Проходим по каждому объявлению
for item in items:
    # Получаем заголовок, цену и ссылку для каждого объявления
    title = item.find_element_by_class_name("snippet-link").text
    price = item.find_element_by_class_name("snippet-price").text
    link = item.find_element_by_class_name("snippet-link").get_attribute("href")

    # Выводим результаты
    print("Заголовок:", title)
    print("Цена:", price)
    print("Ссылка:", link)
    print("\n")

# Переходим на следующие страницы поиска
next_page = driver.find_element_by_class_name("pagination-next")
while next_page.is_enabled():
    next_page.click()
    items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "item"))
    )

    for item in items:
        title = item.find_element_by_class_name("snippet-link").text
        price = item.find_element_by_class_name("snippet-price").text
        link = item.find_element_by_class_name("snippet-link").get_attribute("href")

        print("Заголовок:", title)
        print("Цена:", price)
        print("Ссылка:", link)
        print("\n")

    next_page = driver.find_element_by_class_name("pagination-next")

# Завершаем работу скрипта
driver.quit()

