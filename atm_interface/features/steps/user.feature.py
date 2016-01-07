from behave import given, when, then


def eq(a, b, msg='{a} != {b}'):
    if a != b:
        raise AssertionError(msg.format(a=a, b=b))


@when('I visit home page')
def step_impl(context):
    browser = context.browser
    browser.visit("http://localhost:8081/")


@then('I should see keyboard with input')
def step_impl(context):
    browser = context.browser
    browser.cookies.delete()
    if not browser.is_element_present_by_css('form') and not browser.is_element_present_by_css('.button-set'):
        raise AssertionError("Login page isn't shown")


@given('unlogged user by card number')
def step_impl(context):
    browser = context.browser


@when('I gave not valid data')
def step_impl(context):
    browser = context.browser
    browser.visit("http://localhost:8081/")
    for i in range(1, 3):
        browser.find_by_value('1').first.click()
    browser.find_by_value('OK').first.click()


@when('I gave valid data')
def step_impl(context):
    browser = context.browser
    for i in range(1, 16):
        browser.find_by_value('1').first.click()
    browser.find_by_value('OK').first.click()


@then('I should see login form and see error message')
def step_impl(context):
    browser = context.browser
    browser.cookies.delete()
    if not browser.is_element_present_by_value('form'):
        raise AssertionError("Login page isn't shown")


@then('I should see pin page')
def step_impl(context):
    browser = context.browser
    eq(browser.url, 'http://localhost:8081/pin/')

