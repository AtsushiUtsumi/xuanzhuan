# このファイルは「XuanZhuan」のドメインレイヤーに入れても良いかもしれない
class TestCase:
    def __init__(self, description, function_name):
        self.description = description
        self.function_name = function_name

class UseCase:
    def __init__(self, description, function_name, test_case_list: list[TestCase] = [], di=[],use_log=True):
        self.description = description
        self.function_name = function_name
        self.use_log = use_log
        self.di = di
        self.test_case_list = test_case_list
        for i in self.test_case_list:
            print('登録されたテストケース:' + i.description)
    def add_test_case(self, test_case: TestCase):
        self.test_case_list.append(test_case)
        return