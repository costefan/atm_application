from splinter.browser import Browser


def before_all(context):
    context.browser = Browser(context.config.browser or 'firefox')


def after_all(context):
    context.browser.quit()



