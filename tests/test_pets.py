"""Tests of pets package functionality.
"""
import pets

def test__version__():
    assert pets.__version__ == '0.0'

def test__all__():
    assert pets.__all__ == ['list_all']
    
def test_list_all():
    assert pets.list_all() == ['dog', 'cat']
