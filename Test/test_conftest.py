# conftest.py

import pytest
import requests

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())

#Imagine that you’ve written a test suite for code that deals with API calls.
#You want to ensure that the test suite doesn’t make any real network calls
#even if someone accidentally writes a test that does so.