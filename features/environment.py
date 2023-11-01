import behave
from allure_behave.utils import scenario_name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from support.logger import logger


# behave -f allure_behave.formatter:AllureFormatter -o test_results ./features/tests/Task 1.feature
# allure serve test_results/

def browser_init(context):
# def browser_init(context, scenario_name):  # add scenario_name if you want to use it in Browserstack
    """
    :param context: Behave context
    """

    # Chrome  Setup
    # service = Service(executable_path='/Users/nilufayesmin/Downloads/Internship/chromedriver')
    # context.driver = webdriver.Chrome(service=service)

    # --- Chrome_browser test --- #

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)


    # --- Cross-browser FIREFOX test --- #

    ## service = Service(executable_path=r'C:\Users\Al-FALAH\Careerist\python-selenium-automation\Internship June 2nd Batch\Driver\chrome-win64geckodriver.exe')
    ## context.driver = webdriver.Firefox(service=service)

    # context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    # --- HEADLESS MODE --- #
    # options = webdriver.ChromeOptions()
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1000,1000')
    # service = Service(executable_path=r'/Users/nilufayesmin/Downloads/Internship/chromedriver')
    # context.driver = webdriver.Chrome(options=options,service=service)

    ### OTHER BROWSERS ###
    # service = Service(executable_path='/Users/balamurugann/Automation_QA/sb_python-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    ## BROWSERSTACK ###

    # bs_user = 'nilufayesmin_xelEuD'
    # bs_key = 'KYYqtqbbDh3qTy798Pxs'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     "debug": "true",
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    # context.driver.maximize_window()


# # --- mobile emulation --- # #

    mobile_emulation = {"deviceName": "Samsung Galaxy S8+"}

    options = webdriver.ChromeOptions()

    options.add_experimental_option("mobileEmulation", mobile_emulation)

    service = Service(
        executable_path=r'/Users/nilufayesmin/Downloads/Internship/chromedriver')
    context.driver = webdriver.Chrome(
        options = options,
        service=service
    )

# # --- mobile view for browserstack--- # #

    # bs_user = 'nilufayesmin_xelEuD'
    # bs_key = 'KYYqtqbbDh3qTy798Pxs'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #
    # "osVersion": "8.1",
    # "deviceName": "Samsung Galaxy Note 9",
    # "local": "false",
    # "debug": "true",
    # 'browserName': 'Chrome',
    # 'sessionName': scenario_name
    #
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
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

