import allure
import pytest


@allure.id("611")
@allure.tag("regress")
@allure.title("Отображение активных акций в каталоге")
@allure.label("owner", "Елена")
@allure.feature("Каталог")
@allure.story("Акции")
def test_catalog_1():
    with allure.step("Откройте страницу каталога во время активной акции"):
        with allure.step("Expected Result"):
            with allure.step("Товары, участвующие в акции, отмечены визуальной меткой («-20%», «Sale», «Акция»)"):
                pass
            with allure.step("Отображаются две цены - старая (зачёркнутая) и новая (со скидкой)"):
                pass
    with allure.step("Наведите курсор/тапните по карточке товара"):
        with allure.step("Expected Result"):
            with allure.step("Отображается подробная информация об акции (если предусмотрено: срок, условия)"):
                pass
    with allure.step("Откройте карточку акционного товара"):
        with allure.step("Expected Result"):
            with allure.step("Скидка и метка акции сохраняются"):
                pass
            with allure.step("Цены и расчёт скидки идентичны каталогу"):
                pass
            with allure.step("Ошибок округления и несоответствия процентов нет"):
                pass

@allure.id("612")
@allure.tag("regress")
@allure.title("Корректность расчёта скидки на товар")
@allure.label("owner", "Елена")
@allure.feature("Каталог")
@allure.story("Акции")
def test_catalog_2():
    with allure.step("Найдите товар со скидкой"):
        with allure.step("Expected Result"):
            with allure.step("На карточке товара отображается метка скидки (например, «-20%»)"):
                pass
            with allure.step("Старая цена отображается зачёркнутой, новая - выделена цветом"):
                pass
    with allure.step("Проверьте арифметику расчёта скидки"):
        with allure.step("Expected Result"):
            with allure.step("Новая цена соответствует формуле: новая = старая × (1 - скидка/100)"):
                pass
            with allure.step("Разница в цене не превышает округление в пределах 1 рубля"):
                pass
    with allure.step("Откройте карточку товара"):
        with allure.step("Expected Result"):
            with allure.step("Процент и итоговая цена совпадают с данными в каталоге"):
                pass
            with allure.step("Никаких расхождений между каталогом и карточкой нет"):
                pass

@allure.id("598")
@allure.tag("regress")
@allure.title("Переход из главного меню в раздел каталога")
@allure.label("owner", "Елена")
@allure.feature("Каталог")
@allure.story("Навигация")
def test_catalog_3():
    with allure.step("Откройте главную страницу интернет-магазина"):
        with allure.step("Expected Result"):
            with allure.step("Главное меню отображается в верхней части страницы"):
                pass
    with allure.step("Нажмите на пункт меню «Каталог»"):
        with allure.step("Expected Result"):
            with allure.step("Пользователь перенаправлен на страницу каталога"):
                pass
            with allure.step("URL изменился на /catalog или аналогичный"):
                pass
            with allure.step("Страница каталога отображает список категорий или товаров без ошибок загрузки"):
                pass
              
@allure.id("599")
@allure.tag("regress")
@allure.title("Переход по категориям каталога")
@allure.label("owner", "Елена")
@allure.feature("Каталог")
@allure.story("Навигация")
def test_catalog_4():
    with allure.step("На странице каталога выберите категорию (например, «Одежда»)"):
        with allure.step("Expected Result"):
            with allure.step("Отображается список товаров выбранной категории"):
                pass
            with allure.step("Заголовок страницы соответствует названию категории"):
                pass
    with allure.step("Перейдите в другую категорию (например, «Обувь»)"):
        with allure.step("Expected Result"):
            with allure.step("Список товаров обновляется, отображая только товары из новой категории"):
                pass
            with allure.step("URL меняется в соответствии с категорией (например, /catalog/shoes)"):
                pass
            with allure.step("Ошибок загрузки не возникает"):
                pass
              
@allure.id("609")
@allure.tag("regress")
@allure.title("Сортировка товаров по популярности")
@allure.label("owner", "Елена")
@allure.feature("Каталог")
@allure.story("Сортировка")
def test_catalog_5():
    with allure.step("Выберите сортировку «По популярности»"):
        with allure.step("Expected Result"):
            with allure.step("Товары сортируются в порядке убывания рейтинга или количества покупок"):
                pass
            with allure.step("Порядок не нарушается при прокрутке или смене страницы"):
                pass
    with allure.step("Обновите страницу"):
        with allure.step("Expected Result"):
            with allure.step("Порядок сортировки сохраняется (если предусмотрено системой)"):
                pass
            with allure.step("Отображаемые значения рейтинга корректны и соответствуют данным в базе"):
                pass
