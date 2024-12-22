import pytest
import yaml
import os


# 读取YAML文件并返回测试用例数据
def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


# 使用 pytest_generate_tests 钩子动态生成测试用例
def pytest_generate_tests(metafunc):
    if 'test_case' in metafunc.fixturenames:
        test_file = metafunc.definition.fspath.purebasename
        operation_type = test_file.split('_')[1]  # 假设文件名格式是 test_{operation}.py
        yaml_file = os.path.join(os.path.dirname(__file__), 'data', f'math_operations_{operation_type}.yaml')

        if os.path.exists(yaml_file):
            yaml_data = read_yaml(yaml_file)
            metafunc.parametrize("test_case", yaml_data)
        else:
            raise FileNotFoundError(f"No such file or directory: '{yaml_file}'")
