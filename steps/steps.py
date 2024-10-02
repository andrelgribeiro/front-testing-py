from behave import given, when, then
from selenium import webdriver
from page_objects.front_page_objects import FrontPageObjects

@given('que estou na página "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.page = FrontPageObjects(context.driver)
    context.driver.get(url)

@when('eu marco o primeiro checkbox')
def step_impl(context):
    context.page.check_first_checkbox()

@then('o primeiro checkbox deve estar marcado')
def step_impl(context):
    assert context.page.is_first_checkbox_checked()

@when('eu desmarco o primeiro checkbox')
def step_impl(context):
    context.page.uncheck_first_checkbox()

@then('o primeiro checkbox deve estar desmarcado')
def step_impl(context):
    assert not context.page.is_first_checkbox_checked()

@when('eu arrasto o elemento A para a posição do elemento B')
def step_impl(context):
    context.page.drag_and_drop()

@then('os elementos devem trocar de posição')
def step_impl(context):
    assert context.page.is_drag_successful()
