import pytest


class WebDriver:
    def open(self, url):
        self.url = url

    def close(self):
        ...

    @property
    def text(self):
        return self.pages[self.url]

    pages = {
        "https://example.com": "Hello! I am the homepage",
        "https://example.com/about": "About us: We write tests",
    }


def create_webdriver(browser_name):
    """create a new browser instance and return it"""
    return WebDriver()


@pytest.fixture(scope="module", params=["firefox", "chrome", "edge", "safari"])
def browser_name(request):
    # `request` is a special value provided by pytest
    # that lets you see the test metadata
    return request.param


@pytest.fixture(scope="module")
def webdriver(browser_name):
    webdriver_instance = create_webdriver(browser_name)
    try:
        yield webdriver_instance
    finally:
        webdriver_instance.close()


def test_homepage(webdriver):
    webdriver.open("https://example.com")
    assert "Hello!" in webdriver.text


def test_about_page(webdriver):
    webdriver.open("https://example.com/about")
    assert "About us" in webdriver.text
