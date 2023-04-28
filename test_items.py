import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_cart_button(browser):
    browser.get(link)
    time.sleep(5)
    cart_button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary")

    assert cart_button.is_displayed(), "Add to cart button is not found / Кнопка ДОБАВИТЬ В КОРЗИНУ не найдена"
