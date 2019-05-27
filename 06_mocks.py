import requests
import pytest
from unittest import mock
from bs4 import BeautifulSoup

EXAMPLE_CONTENT = """
<!doctype html>
<h1>Cats</j1>
<ul>
    <li>
        Cat 1: <img src="cat1.png">
    </li>
    <li>
        Cat 2: <img src="cat2.png">
    </li>
</ul>
"""


def get_image_urls(url):
    response = requests.get(url)
    response.raise_for_status()
    images = BeautifulSoup(response.content, features="lxml").find_all("img")
    return [image["src"] for image in images if image["src"]]


def test_get_image_urls():
    with mock.patch.object(requests.Session, "request") as mock_request:
        mock_request().content = EXAMPLE_CONTENT

        assert ["cat1.png", "cat2.png"] == get_image_urls("http://cats.example.com")


# after


@pytest.fixture
def mock_requests():
    with mock.patch.object(requests.Session, "request") as mock_request:
        mock_request().content = '<img src="cat1.png"> <img src="cat2.png">'
        yield


@pytest.mark.usefixtures("mock_requests")
def test_get_image_urls_2():
    assert ["cat1.png", "cat2.png"] == get_image_urls("http://cats.example.com")
