from file_workers import read_from_file
import pytest


def test_read_from_file():
    
    test_data=['one\n', 'two\n', 'three\n']
    assert test_data==read_from_file('tests/testfile.txt')
