# buggy_example.py
# Issue 1: Function returns wrong result (logic bug)
# Issue 2: Missing docstring (style issue)

def add_numbers(a, b):
    # Should return a + b, but mistakenly returns a - b
    return a - b

# This function is not used anywhere (potential dead code)
def unused_function():
    print("This function is unused.")