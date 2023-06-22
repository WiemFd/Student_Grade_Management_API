import pytest
from rest_framework.test import APIClient


@pytest.fixture(scope="function")
def client():
    """
    Fixture to provide an API client
    :return: APIClient
    """
    yield APIClient()
