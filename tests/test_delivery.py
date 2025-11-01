import allure
import pytest


#@allure.id("673")
@allure.tag("regress")
@allure.title("Выбор временного окна доставки")
@allure.label("owner", "Мария")
@allure.feature("Доставка")
@allure.story("Выбор способа доставки")
def test_delivery_1():
    with allure.step("В разделе выбора времени откройте список доступных временных интервалов (например, 10:00–14:00, 14:00–18:00)"):
        with allure.step("Expected Result"):
            with allure.step("Список отображает только актуальные и доступные слоты"):
                pass
    with allure.step("Выберите одно временное окно"):
        with allure.step("Expected Result"):
            with allure.step("Выбранный слот подсвечен"):
                pass
            with allure.step("В блоке итогов заказа отображается выбранное время доставки"):
                pass
    with allure.step("Обновите страницу или перейдите на шаг подтверждения"):
        with allure.step("Expected Result"):
            with allure.step("Выбранный временной интервал сохраняется и корректно отображается в заказе"):
                pass

#@allure.id("675")
@allure.tag("regress")
@allure.title("Отображение трекинг-номера заказа")
@allure.label("owner", "Мария")
@allure.feature("Доставка")
@allure.story("Отслеживание статуса доставки")
def test_delivery_2():
    with allure.step("Перейдите в раздел «Мои заказы» и откройте детали оформленного заказа"):
        with allure.step("Expected Result"):
            with allure.step("В карточке заказа отображается трекинг-номер (например, «Track №123456789»)"):
                pass
            with allure.step("Рядом с номером присутствует ссылка «Отследить»"):
                pass
    with allure.step("Нажмите на ссылку «Отследить»"):
        with allure.step("Expected Result"):
            with allure.step("Выполняется переход на страницу трекинга (внешнюю или внутреннюю)"):
                pass
            with allure.step("Страница открывается без ошибок, отображает статус посылки"):
                pass
    with allure.step("Проверьте поведение при отсутствии номера"):
        with allure.step("Expected Result"):
            with allure.step("Если трекинг-номер ещё не присвоен, отображается сообщение «Трекинг-номер появится после передачи в службу доставки»"):
                pass

#@allure.id("668")
@allure.tag("regress")
@allure.title("Расчёт стоимости доставки по указанному адресу")
@allure.label("owner", "Мария")
@allure.feature("Доставка")
@allure.story("Расчёт стоимости и сроков")
def test_delivery_3():
    with allure.step("Введите валидный адрес (город, улица, дом, индекс, регион)"):
        with allure.step("Expected Result"):
            with allure.step("Адрес проходит валидацию без ошибок"):
                pass
    with allure.step("Запросите расчёт стоимости доставки (автоматически или кнопкой «Рассчитать»)"):
        with allure.step("Expected Result"):
            with allure.step("Появляется рассчитанная стоимость доставки для введённого адреса"):
                pass
            with allure.step("Сроки доставки отображаются (например, «2–4 дня»)"):
                pass
    with allure.step("Проверьте перенос суммы доставки в сводку заказа"):
        with allure.step("Expected Result"):
            with allure.step("В блоке итогов видна строка «Доставка» с рассчитанной суммой"):
                pass
            with allure.step("Итого заказа увеличивается на стоимость доставки"):
                pass

#@allure.id("669")
@allure.tag("regress")
@allure.title("Применение бесплатной доставки при достижении порога суммы")
@allure.label("owner", "Мария")
@allure.feature("Доставка")
@allure.story("Расчёт стоимости и сроков")
def test_delivery_4():
    with allure.step("Проверьте стоимость доставки при текущей сумме (ниже порога)"):
        with allure.step("Expected Result"):
            with allure.step("В итогах отображается положительная стоимость доставки"):
                pass
    with allure.step("Увеличьте сумму корзины (добавьте товар/увеличьте количество), чтобы превысить порог"):
        with allure.step("Expected Result"):
            with allure.step("После пересчёта строка «Доставка» меняется на «0»/«Бесплатно»"):
                pass
            with allure.step("Итого заказа уменьшается на ранее начисленную стоимость доставки"):
                pass
    with allure.step("Обновите страницу/перейдите к подтверждению"):
        with allure.step("Expected Result"):
            with allure.step("Статус «Бесплатная доставка» сохраняется в сводке и на финальной странице"):
                pass
