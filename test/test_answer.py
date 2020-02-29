import pytest
import request as answer


def test_file_answer():
    assert answer.file_answer() == str("<Response [200]>")

def test_file_path():
    assert answer.file_path() == True