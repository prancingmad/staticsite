# python
import pytest
from extract_title import extract_title

def test_extract_title_basic():
    assert extract_title("# Tolkien Fan Club") == "Tolkien Fan Club"

def test_extract_title_raises_without_h1():
    with pytest.raises(Exception):
        extract_title("## Not a title")