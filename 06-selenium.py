import pytest

@pytest.fixture(scope="session")
def webdriver_process():
    ...

@pytest.fixture()
def webdriver(webdriver_process):
    webdriver_process.new_window()
    return webdriver_process


@pytest.fixture(scope="session")
def database_connection():
    ...


@pytest.fixture
def database(database_connection):
    try:
        yield database_connection
    finally:
        ... # truncate necessary tables


@pytest.fixture(scope="session")
def redis_connection():
    ...

@pytest.fixture
def redis_cache(redis_connection, django_settings):
    cache_backend = ...
    django_settings = ...