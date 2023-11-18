# このファイルは「XuanZhuan」のドメインレイヤーに入れても良いかもしれない

from xuanzhuan.layer.application.use_case import UseCase

class ApplicationService:
    def readme() -> str:
        return 'アプリケーションサービスのクラス'
    def __str__(self) -> str:
        out = ''
        for u in self.use_case_list:
            out += u.description + '\n'
        return out
    def __init__(self, root_dir, description):
        self.use_case_list = list()
        self.root_dir = root_dir
        self.description = description
    def add_use_case(self, use_case: UseCase):
        self.use_case_list.append(use_case)
        return
