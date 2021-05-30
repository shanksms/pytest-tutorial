import pytest
from marker.myapp.sample import add
import sys


@pytest.mark.skip
def test_add_number():
    assert add(1, 2) == 3


@pytest.mark.skipif(sys.version_info > (3, 0), reason="only runs with latest version")
def test_add_str():
    assert add("a", "b") == "ab"

