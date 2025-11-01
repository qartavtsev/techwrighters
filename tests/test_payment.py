import allure
import pytest


@allure.id("667")
@allure.tag("regress")
@allure.title("Частичный возврат суммы по отдельным позициям заказа")
@allure.label("owner", "Мария")
@allure.feature("Оплата")
@allure.story("Возвраты")
def test_payment_1():
    with allure.step("Откройте детали заказа и выберите позиции/количество для частичного возврата"):
        with allure.step("Expected Result"):
            with allure.step("Интерфейс позволяет отметить конкретные позиции и их количество"):
                pass
    with allure.step("Инициируйте частичный возврат"):
        with allure.step("Expected Result"):
            with allure.step("Рассчитана сумма возврата = сумма выбранных позиций (с учётом скидок)"):
                pass
            with allure.step("Запрос на частичный возврат отправлен провайдеру"):
                pass
    with allure.step("Проверьте статусы платежа и заказа"):
        with allure.step("Expected Result"):
            with allure.step("Платёж отражает частичный возврат («Partially Refunded»)"):
                pass
            with allure.step("В заказе отображается операция частичного возврата и актуальная «Итого»"):
                pass
            with allure.step("Остаток по заказу остаётся «Оплачен» на непрерывнутую часть"):
                pass

@allure.id("662")
@allure.tag("regress")
@allure.title("Отмена оплаты пользователем у провайдера и возврат в магазин")
@allure.label("owner", "Мария")
@allure.feature("Оплата")
@allure.story("Онлайн-оплата")
def test_payment_2():
    with allure.step("На платёжной странице провайдера нажмите «Отмена»"):
        with allure.step("Expected Result"):
            with allure.step("Выполняется редирект на cancel-URL магазина"):
                pass
    with allure.step("Проверьте состояние заказа в магазине"):
        with allure.step("Expected Result"):
            with allure.step("Статус заказа остаётся «Ожидает оплаты»/«Отменён» (по бизнес-логике), но не «Оплачен»"):
                pass
            with allure.step("Появляется понятное сообщение «Оплата отменена пользователем»"):
                pass
            with allure.step("Доступна кнопка «Оплатить позже»/«Повторить оплату»"):
                pass

@allure.id("663")
@allure.tag("regress")
@allure.title("Повторная попытка оплаты по созданному заказу")
@allure.label("owner", "Мария")
@allure.feature("Оплата")
@allure.story("Онлайн-оплата")
def test_payment_3():
    with allure.step("Откройте детали заказа в «Мои заказы» и нажмите «Оплатить»"):
        with allure.step("Expected Result"):
            with allure.step("Выполняется редирект на платёжную страницу (или встраивается виджет)"):
                pass
    with allure.step("Выполните оплату валидными тестовыми реквизитами (successful)"):
        with allure.step("Expected Result"):
            with allure.step("Провайдер возвращает success, редирект на success-URL"):
                pass
    with allure.step("Проверьте состояние заказа в магазине"):
        with allure.step("Expected Result"):
            with allure.step("Статус заказа обновлён на «Оплачен»"):
                pass
            with allure.step("История платежей содержит две записи: неуспешную/отменённую и успешную"):
                pass
            with allure.step("Пользователь видит подтверждение и чек/квитанцию (если предусмотрено)"):
                pass
