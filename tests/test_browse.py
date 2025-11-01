import allure
import pytest


#@allure.id("637")
@allure.tag("regress")
@allure.title("Добавление товара в избранное")
@allure.label("owner", "Иван")
@allure.feature("Поиск, сравнение и избранное")
@allure.story("Избранное")
def test_method():
    with allure.step("Найдите товар в каталоге и нажмите на иконку «Сердце»"):
        with allure.step("Expected Result"):
            with allure.step("Иконка меняет цвет или состояние (например, становится закрашенной)"):
                pass
            with allure.step("Появляется уведомление «Товар добавлен в избранное»"):
                pass
    with allure.step("Перейдите на страницу избранного"):
        with allure.step("Expected Result"):
            with allure.step("Добавленный товар отображается в списке избранных товаров"):
                pass
            with allure.step("Все данные (название, цена, фото) отображаются корректно"):
                pass

#@allure.id("630")
@allure.tag("regress", "smoke")
@allure.title("Отображение подсказок при вводе текста в строке поиска")
@allure.label("owner", "Иван")
@allure.feature("Поиск, сравнение и избранное")
@allure.story("Подсказки и автодополнение")
def test_method():
    with allure.step("Начните вводить запрос в строке поиска (например, «тел»)"):
        with allure.step("Expected Result"):
            with allure.step("Под строкой поиска появляется выпадающий список подсказок"):
                pass
            with allure.step("Подсказки содержат совпадения по названию товара («телефон», «телевизор»), категории и бренду"):
                pass
    with allure.step("Выберите одну из подсказок"):
        with allure.step("Expected Result"):
            with allure.step("Происходит переход на страницу соответствующего товара или категории"):
                pass
            with allure.step("В строке поиска отображается выбранное значение"):
                pass
            with allure.step("Ошибок при загрузке страницы не возникает"):
                pass
