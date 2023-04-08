from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Joseph", "Smith") == "Smith; Joseph"
    assert make_full_name("Russell", "Nelson") == "Nelson; Russell"
    assert make_full_name("Thomas", "Monson") == "Monson; Thomas"
    assert make_full_name("Gordon", "Hinckley") == "Hinckley; Gordon"
    assert make_full_name("Howard", "Hunter") == "Hunter; Howard"

def test_extract_family_name():
    assert extract_family_name("Smith; Joseph") == "Smith"
    assert extract_family_name("Nelson; Russell") == "Nelson"
    assert extract_family_name("Monson; Thomas") == "Monson"
    assert extract_family_name("Hinckley; Gordon") == "Hinckley"
    assert extract_family_name("Hunter; Howard") == "Hunter"


def test_extract_given_name():
    assert extract_given_name("Smith; Joseph") == "Joseph"
    assert extract_given_name("Nelson; Russell") == "Russell"
    assert extract_given_name("Monson; Thomas") == "Thomas"
    assert extract_given_name("Hinckley; Gordon") == "Gordon"
    assert extract_given_name("Hunter; Howard") == "Howard"




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])