# test_math_ops.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_add_pass():
    assert add(2, 3) == 5  # ✅ This will pass

def test_subtract_fail():
    assert subtract(10, 4) == 3  # ❌ This will fail (actual result is 6)