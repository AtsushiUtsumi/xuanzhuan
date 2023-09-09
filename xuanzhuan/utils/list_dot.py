def _appended_list(l: list[str], s: str) -> list[str]:
    ret = list()
    for i in l:
        ret.append(i)
    ret.append(s)
    return ret

class _Productor():
    def __init__(self, ll: list[str]):
        self.value = list()
        for i in ll:
            tmp = list()
            tmp.append(i)
            self.value.append(tmp)
        pass
    def __mul__(self, other: list[str]):
        tmp = list()
        for o in other:
            for v in self.value:
                tmp.append(_appended_list(v, o))
        self.value = tmp
        return self
    

# 外部公開するのはこのメソッドのみにしたい
def list_dot(list_list: list[list[str]]):
    ret = []
    x = _Productor(list_list[0])
    for l in list_list[1:]:
        x = x * l
    for i in x.value:
        ret.append(i)
    return ret

for i in list_dot([['A', 'B'],['C', 'D'],['E', 'F']]):
    print(i)