from typing import List
from unittest.mock import MagicMock

import pytest
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

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


@dataclass
class MockRequest:
    method: str
    url: str
    args: tuple
    kwargs: dict


class RequestsMock:
    def __init__(self):
        self.captured_requests: List[MockRequest] = []

    def request(self, method, url, *args, **kwargs):
        self.captured_requests.append(
            MockRequest(method=method, url=url, args=args, kwargs=kwargs)
        )
        response = MagicMock(content=EXAMPLE_CONTENT)
        return response


@pytest.fixture
def mock_requests(monkeypatch):
    request_mock = RequestsMock()
    monkeypatch.setattr(requests.Session, "request", request_mock.request)
    return request_mock


@pytest.fixture
def captured_requests(mock_requests):
    return mock_requests.captured_requests


def get_image_urls(url):
    response = requests.get(url)
    response.raise_for_status()
    images = BeautifulSoup(response.content, features="lxml").find_all("img")
    return [image["src"] for image in images if image["src"]]


def test_get_image_urls_3(captured_requests):
    assert ["cat1.png", "cat2.png"] == get_image_urls("http://cats.example.com")
    assert len(captured_requests) == 1
    assert captured_requests[0].method == "get"
    assert captured_requests[0].url == "http://cats.example.com"
