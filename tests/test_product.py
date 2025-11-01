import allure
import pytest


@allure.id("613")
@allure.tag("regress")
@allure.title("Отображение информации о товаре (название, описание, фото, цена)")
@allure.label("owner", "Елена")
@allure.feature("Товар")
@allure.story("Карточка товара")
def test_product_1():
    with allure.step("Откройте карточку любого товара из каталога"):
        with allure.step("Expected Result"):
            with allure.step("На странице отображаются: название товара, краткое и полное описание, цена, основное фото"):
                pass
            with allure.step("Все данные соответствуют информации из базы"):
                pass
    with allure.step("Проверьте корректность форматирования цены"):
        with allure.step("Expected Result"):
            with allure.step("Цена отображается в нужной валюте с правильным разделением тысяч"):
                pass
    with allure.step("Проверьте наличие дополнительных характеристик (бренд, артикул, материал и т.д.)"):
        with allure.step("Expected Result"):
            with allure.step("Данные присутствуют и отображаются в виде таблицы или списка характеристик"):
                pass
            with allure.step("Нет пустых или некорректных полей"):
                pass

@allure.id("614")
@allure.tag("regress")
@allure.title("Переключение изображений в галерее товара")
@allure.label("owner", "Елена")
@allure.feature("Товар")
@allure.story("Карточка товара")
def test_product_2():
    with allure.step("Откройте карточку товара с несколькими изображениями"):
        with allure.step("Expected Result"):
            with allure.step("Основное изображение отображается по умолчанию"):
                pass
            with allure.step("Под ним/рядом присутствуют миниатюры дополнительных изображений"):
                pass
    with allure.step("Кликните по миниатюре другого фото"):
        with allure.step("Expected Result"):
            with allure.step("Основное изображение обновляется на выбранное"):
                pass
            with allure.step("Нет задержек загрузки или искажений пропорций"):
                pass
    with allure.step("Используйте стрелки навигации (если есть)"):
        with allure.step("Expected Result"):
            with allure.step("Изображения листаются в обе стороны"):
                pass
            with allure.step("Галерея возвращается к первому фото после последнего (если предусмотрено циклическое переключение)"):
                pass

@allure.id("622")
@allure.tag("regress")
@allure.title("Отображение отзывов на товар")
@allure.label("owner", "Елена")
@allure.feature("Товар")
@allure.story("Отзывы")
def test_product_3():
    with allure.step("Откройте карточку товара"):
        with allure.step("Expected Result"):
            with allure.step("Отображается блок «Отзывы» или аналогичный"):
                pass
            with allure.step("В блоке видны автор, дата, оценка и текст отзыва"):
                pass
    with allure.step("Проверьте формат отображения даты и имени"):
        with allure.step("Expected Result"):
            with allure.step("Дата отображается в формате ДД.ММ.ГГГГ"):
                pass
            with allure.step("Имя пользователя или его псевдоним отображается корректно"):
                pass
    with allure.step("Проверьте, что при отсутствии отзывов отображается сообщение «Отзывов пока нет»"):
        with allure.step("Expected Result"):
            with allure.step("Страница отображается без ошибок"):
                pass
            with allure.step("Пользователь может перейти к форме «Оставить отзыв» (если доступна)"):
                pass
              
@allure.id("619")
@allure.tag("regress")
@allure.title("Отображение рейтинга товара")
@allure.label("owner", "Елена")
@allure.feature("Товар")
@allure.story("Рейтинг")
def test_product_4():
    with allure.step("Откройте каталог товаров"):
        with allure.step("Expected Result"):
            with allure.step("У товаров, у которых есть оценки, отображаются звёзды или числовое значение рейтинга"):
                pass
            with allure.step("Рейтинг отображается корректно, без округления сверх допуска (например, 4.5, а не 5)"):
                pass
    with allure.step("Перейдите в карточку товара"):
        with allure.step("Expected Result"):
            with allure.step("Рейтинг дублируется под названием товара"):
                pass
            with allure.step("Отображается среднее значение и общее количество отзывов"):
                pass
    with allure.step("Проверьте, что при отсутствии оценок отображается текст «Нет оценок» или пустые звёзды"):
        with allure.step("Expected Result"):
            with allure.step("Страница отображается без ошибок, рейтинг = 0 или не отображается вовсе"):
                pass
