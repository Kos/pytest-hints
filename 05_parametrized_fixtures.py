from time import sleep

import pytest
from selenium.webdriver import Firefox, Chrome

# TODO: run multiple browsers
# TODO: make sure the browser is efficeint
# TODO: make sure each test gets the browser in a clean state


@pytest.fixture
def webdriver():
    webdriver_instance = Firefox()
    yield webdriver_instance
    sleep(0.5)
    webdriver_instance.close()


def test_example_site(webdriver):
    webdriver.get("https://example.com")
    assert "illustrative examples" in webdriver.page_source


def test_pywaw(webdriver):
    webdriver.get("http://pywaw.org")
    assert "cykliczne spotkania pasjonatów" in webdriver.page_source
