from time import sleep

import pytest
from selenium.webdriver import Firefox, Chrome


@pytest.fixture(scope="module", params=["firefox", "chrome"])
def browser_name(request):
    # `request` is a special value provided by pytest
    # that lets you see the test metadata
    return request.param


@pytest.fixture(scope="module")
def webdriver_instance(browser_name):
    if browser_name == "firefox":
        driver = Firefox()
    elif browser_name == "chrome":
        driver = Chrome()
    else:
        raise Exception(f"Unsupported browser: {browser_name}")

    try:
        yield driver
    finally:
        driver.close()


@pytest.fixture
def webdriver(webdriver_instance):
    try:
        yield webdriver_instance
        sleep(0.5)
    finally:
        webdriver_instance.delete_all_cookies()
        webdriver_instance.get("about:blank")


def test_example_site(webdriver):
    webdriver.get("https://example.com")
    assert "illustrative examples" in webdriver.page_source


def test_pywaw(webdriver):
    webdriver.get("http://pywaw.org")
    assert "cykliczne spotkania pasjonatów" in webdriver.page_source
