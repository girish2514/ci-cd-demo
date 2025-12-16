from calculator import add

def test_add():
    # This is the test. It asserts that 2 + 3 MUST equal 5.
    assert add(2, 3) == 5
    assert add(10, 20) == 30
