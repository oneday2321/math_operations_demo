# -*- coding: UTF-8 -*-
import pytest
import allure


@allure.feature("算数运算")
class TestSubtraction:

    def perform_operation(self,operation, a, b):
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
    def check_result(self,actual_result, expected_result):
        assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

    @allure.title('Operation: {test_case[Operation]}')
    def test_subtraction(self,test_case):
        result = self.perform_operation(test_case['Operation'], test_case['A'], test_case['B'])
        self.check_result(result, test_case['ExpectedResult'])
