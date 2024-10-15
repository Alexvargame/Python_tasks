import pytest
import requests
from stuff import *
@pytest.fixture()
def prepped_stuff():
    my_stuff = Stuff()
    my_stuff.prep()
    def fin():
        my_stuff.finish()
    requests.addfinalizer(fin)
    return my_stuff




def test_foo_updates(prepped_stuff):
    assert 1 == prepped_stuff.foo
    my_stuff.foo = 30000
    assert my_stuff.foo == 30000


def test_bar_updates(prepped_stuff):
    assert 2 == prepped_stuff.bar
    my_stuff.bar = 42
    assert 42 == my_stuff.bar
