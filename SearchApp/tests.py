from django.test import TestCase
# Create your tests here.


def get_index():
    return 'Hello'

def test_get_index():
    assert get_index() == 'Hello'
