import pytest
import request as answer

result = str("<Response [200]>")

def test_add():
    assert answer.file_answer() == result