from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Запускаем браузер
    context = browser.new_context()  # Создаем новый контекст
    page = context.new_page()  # Открываем новую страницу
    page.goto("https://yandex.ru")  # Переходим на сайт
    print(page.title())  # Печатаем заголовок страницы
    page.screenshot(path="yandex_screenshot.png")  # Делаем скриншот
    context.close()  # Закрываем контекст
    browser.close()  # Закрываем браузер

with sync_playwright() as playwright:
    run(playwright)