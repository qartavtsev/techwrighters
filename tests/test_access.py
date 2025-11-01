import allure
import pytest


#@allure.id("571")
@allure.tag("regress", "smoke")
@allure.title("Успешное восстановление пароля через email")
@allure.label("owner", "Анна")
@allure.feature("Регистрация и авторизация")
@allure.story("Восстановление пароля")
def test_method():
    with allure.step("На странице входа нажмите ссылку «Забыли пароль?»"):
        with allure.step("Expected Result"):
            with allure.step("Открывается страница восстановления пароля с полем «Email»"):
                pass
    with allure.step("Введите корректный зарегистрированный адрес почты и нажмите «Восстановить пароль»"):
        with allure.step("Expected Result"):
            with allure.step("Отправлен запрос на сброс пароля"):
                pass
            with allure.step("Показано уведомление: «Мы отправили письмо с инструкциями"):
                pass
    with allure.step("Откройте письмо и перейдите по ссылке восстановления"):
        with allure.step("Expected Result"):
            with allure.step("Открывается страница задания нового пароля"):
                pass
    with allure.step("Введите новый валидный пароль и его подтверждение, сохраните"):
        with allure.step("Expected Result"):
            with allure.step("Пароль успешно обновлен, отображается уведомление об успехе"):
                pass
            with allure.step("Пользователь перенаправлен на страницу входа и может войти с новым паролем"):
                pass

#@allure.id("564")
@allure.tag("regress")
@allure.title("Валидация обязательных полей формы регистрации")
@allure.label("owner", "Анна")
@allure.feature("Регистрация и авторизация")
@allure.story("Регистрация")
def test_method():
    with allure.step("Откройте страницу регистрации интернет-магазина"):
        with allure.step("Expected Result"):
            with allure.step("Форма регистрации отображается с обязательными полями, помеченными индикатором обязательности (например, «*»)"):
                pass
    with allure.step("Не заполняя ни одно поле, нажмите «Зарегистрироваться»"):
        with allure.step("Expected Result"):
            with allure.step("Появляются сообщения валидации под обязательными полями («Поле обязательно для заполнения»)"):
                pass
            with allure.step("Запрос на создание учетной записи не отправляется; пользователь остается на странице регистрации"):
                pass
    with allure.step("Последовательно заполняйте по одному полю и нажимайте «Зарегистрироваться»"):
        with allure.step("Expected Result"):
            with allure.step("Сообщения валидации исчезают для заполненных полей"):
                pass
            with allure.step("Сообщение валидации сохраняется для первого незаполненного обязательного поля"):
                pass
    with allure.step("Заполните все обязательные поля корректными значениями"):
        with allure.step("Expected Result"):
            with allure.step("Сообщения об ошибках исчезают; кнопка «Зарегистрироваться» становится доступной"):
                pass
