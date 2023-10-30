from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main_reelly(context):
    context.app.main_page.open_main()

@when('Log in to the page')
def log_in_webpage(context):
    context.app.log_in_page.click_on_signin_link()
    sleep(2)
    context.app.log_in_page.input_email("aminilufa71@gmail.com")
    sleep(2)
    context.app.log_in_page.input_password("Runa3271!")
    sleep(2)
    context.app.log_in_page.click_continue()

# @when('Click on off plan at the left side menu')
# def off_plan(context):
#     context.app.off_plan_page.off_plan_menu_web()
#     sleep(3)

@when('Click on off plan from bottom menu')
def off_plan(context):
    context.app.off_plan_page.off_plan_menu_mobile()
    sleep(3)

@when('Verify the right page opens')
def right_page_opens(context):
    context.app.off_plan_page.right_page()
    # context.app.off_plan_page.verify_right_off_plan()
    sleep(3)

@when ('Filter by sale status of Out of Stocks')
def filter_by_sale_status(context):
    context.app.off_plan_page.filter_by_out_of_stock()
    sleep(5)

@then ('Verify each product contains the Out of Stocks tag')
def sale_status_tag(context):
    # context.app.main_page.verify_each_product_contains_sale_status_tag()
    expected_text = 'Out of stock'
    locator = context.app.off_plan_page.Out_Of_Stock_Tag
    context.app.off_plan_page.verify_each_product_contains_sale_status_tag(expected_text, locator)
    sleep(2)