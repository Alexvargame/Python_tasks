import pytest
@pytest.fixture()
def prepped_stuff():
    my_stuff = stuff.Stuff()
    my_stuff.prep()
    def fin():
        my_stuff.finish()
    request.addfinalizer(fin)
    return my_stuff
