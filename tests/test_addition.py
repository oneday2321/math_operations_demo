import pytest

# 执行数学运算
def perform_operation(operation, a, b):
    if operation == 'addition':
        return a + b
    elif operation == 'subtraction':
        return a - b
    elif operation == 'multiplication':
        return a * b
    elif operation == 'division':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# 检查结果
def check_result(actual_result, expected_result):
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

def test_addition(test_case):
    result = perform_operation(test_case['Operation'], test_case['A'], test_case['B'])
    check_result(result, test_case['ExpectedResult'])
