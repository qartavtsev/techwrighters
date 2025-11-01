import allure
import pytest


@allure.id("653")
@allure.tag("regress")
@allure.title("Переключение способа оплаты")
@allure.label("owner", "Мария")
@allure.feature("Заказ")
@allure.story("Выбор способа оплаты")
def test_order_1():
    with allure.step("Выберите первый способ оплаты (например, «Банковская карта»)"):
        with allure.step("Expected Result"):
            with allure.step("Вариант подсвечивается или отмечается как выбранный"):
                pass
            with allure.step("В блоке итогов заказа отображается выбранный способ"):
                pass
    with allure.step("Переключитесь на другой вариант оплаты (например, «Оплата при получении»)"):
        with allure.step("Expected Result"):
            with allure.step("Подсветка и отображаемый способ обновляются"):
                pass
            with allure.step("Ошибок при переключении нет"):
                pass
    with allure.step("Перейдите к следующему шагу"):
        with allure.step("Expected Result"):
            with allure.step("Выбранный способ оплаты сохраняется и отображается в сводке заказа"):
                pass

@allure.id("654")
@allure.tag("regress")
@allure.title("Выбор оплаты при получении")
@allure.label("owner", "Мария")
@allure.feature("Заказ")
@allure.story("Выбор способа оплаты")
def test_order_2():
    with allure.step("На шаге «Оплата» выберите вариант «Оплата при получении»"):
        with allure.step("Expected Result"):
            with allure.step("Способ подсвечен как выбранный"):
                pass
            with allure.step("В блоке итогов отображается «Оплата при получении»"):
                pass
    with allure.step("Перейдите к следующему шагу «Подтверждение заказа»"):
        with allure.step("Expected Result"):
            with allure.step("Способ оплаты при получении сохраняется"):
                pass
            with allure.step("В сводке заказа корректно указано: «Оплата при получении»"):
                pass
    with allure.step("Завершите оформление"):
        with allure.step("Expected Result"):
            with allure.step("Заказ успешно оформлен, без перехода на платёжную страницу"):
                pass
            with allure.step("Пользователь получает подтверждение заказа"):
                pass

@allure.id("656")
@allure.tag("regress")
@allure.title("Отображение корректной сводки заказа (товары, цены, доставка, итоги)")
@allure.label("owner", "Мария")
@allure.feature("Заказ")
@allure.story("Проверка и подтверждение заказа")
def test_order_3():
    with allure.step("Откройте сводку заказа на шаге «Подтверждение»"):
        with allure.step("Expected Result"):
            with allure.step("Отображается список товаров с названием, вариантом (если есть), количеством и ценой за единицу"):
                pass
            with allure.step("Под каждой строкой верно рассчитана сумма позиции = цена * количество"):
                pass
    with allure.step("Проверьте блок стоимости"):
        with allure.step("Expected Result"):
            with allure.step("Отображаются строки: «Сумма товаров», «Скидка по промокоду» (если применялся), «Доставка», «Итого к оплате»"):
                pass
            with allure.step("Итоговая сумма соответствует формуле: сумма товаров – скидки + доставка"):
                pass
    with allure.step("Проверьте блок «Доставка и оплата»"):
        with allure.step("Expected Result"):
            with allure.step("Отображаются выбранный способ доставки, адрес, способ оплаты"):
                pass
            with allure.step("Данные совпадают с выбранными на предыдущих шагах"):
                pass
    with allure.step("Обновите страницу"):
        with allure.step("Expected Result"):
            with allure.step("Сводка заказа отображается неизменной, расчёты не «сбрасываются»"):
                pass
