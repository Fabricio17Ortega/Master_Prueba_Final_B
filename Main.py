from selenium import webdriver
from selenium.webdriver.common.by import By
from db import MongoDriver

driver = webdriver.Chrome()
driver.get("https://popzoneshopec.com/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value=".input--full")
search_box.send_keys("Marvel")

search_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn.btn--narrow.btn--full")
search_button.click()

funko_cards = driver.find_elements(By.CSS_SELECTOR, ".grid.grid--no-gutters.grid--uniform > div.grid__item.small--one-half.medium-up--one-fifth")

mongodb = MongoDriver()

for card in funko_cards:
    try:
        title = card.find_element(By.CSS_SELECTOR, "a > div.product-card__info > div.product-card__name").text
        #kms_y_city = card.find_element(By.CSS_SELECTOR, "a > div.product-card__info > div.product-card__price").text
        price = card.find_element(By.CSS_SELECTOR, "a > div.product-card__info > div.product-card__price").text
        print(title)
        #print(kms_y_city)
        print(f"${price}")

        funko_actual = {
            "title": title,
            #"kms_y_city": kms_y_city,
            "price": price
        }

        mongodb.insert_record(record=funko_actual, username="Marvel")

        print("++++++++++++++++++++++++++++++++")
    except Exception as e:
        print(e)
        print("++++++++++++++++++++++++++++++++")


driver.close()