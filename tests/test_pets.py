"""Tests of pets package functionality.
"""
import pets

def test_list_all():
    assert pets.list_all() == ['dog', 'cat']
