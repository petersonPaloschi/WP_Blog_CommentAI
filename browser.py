from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_browser(browser, headless=False, proxy=None, custom_options=None):

    if browser.lower() == "firefox":

        from selenium.webdriver.firefox.options import Options
        options = Options()

    elif browser.lower() == "chrome":

        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

    if headless:
        options.add_argument("--headless")

    if proxy:
        options.add_argument(f"--proxy-server={proxy}")

    if custom_options:

        for option in custom_options:
            options.add_argument(option)

    if browser.lower() == "firefox":

        web_drive = webdriver.Firefox(options=options)

    elif browser.lower() == "chrome":

        web_drive = webdriver.Chrome(options=options)

    web_drive.implicitly_wait(10)

    return web_drive


def browser_quit(web_drive):

    print("[-] Fechando browser!")
    web_drive.quit()

    return