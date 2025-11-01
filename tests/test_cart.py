import allure
import pytest


#@allure.id("644")
@allure.tag("regress")
@allure.title("Пересчёт суммы при изменении количества товаров")
@allure.label("owner", "Иван")
@allure.feature("Корзина")
@allure.story("Пересчёт итоговой стоимости")
def test_cart_1():
    with allure.step("Увеличьте количество товара (например, с 1 до 2)"):
        with allure.step("Expected Result"):
            with allure.step("Общая сумма обновляется и равна цена * 2"):
                pass
            with allure.step("Изменение суммы происходит без обновления всей страницы"):
                pass
    with allure.step("Уменьшите количество товара (например, с 2 до 1)"):
        with allure.step("Expected Result"):
            with allure.step("Общая сумма уменьшается обратно до цены одного товара"):
                pass
            with allure.step("Пересчёт выполняется мгновенно"):
                pass
    with allure.step("Проверьте итоговую сумму всех товаров"):
        with allure.step("Expected Result"):
            with allure.step("Итог заказа соответствует сумме всех строк корзины"):
                pass
