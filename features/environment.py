from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from support.logger import logger

def browser_init(context):

# --- Chrome_browser test --- #

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    # context.driver.maximize_window()

###____Cross Browser Firefox____###
    # context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


###____ HEADLESS MODE ____ ####
    options = webdriver.ChromeOptions()
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1000, 1000')
    service = Service(r'/Users/nilufayesmin/Downloads/Internship/chromedriver.exe')
    context.driver = webdriver.Chrome (options=options,  service=service)



    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)

def before_scenario(context, scenario):

    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context)
    # browser_init(context, scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()