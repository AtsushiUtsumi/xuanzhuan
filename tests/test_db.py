import pytest

from xuanzhuan.db import create_ld_from_sample_dict

def test_サンプルデータ当たり生成():
    sample = {'name': ['utusmi', 'yamada','tanaka'],'age': ['15', '13'],'sex': ['male', 'female']}
    result = create_ld_from_sample_dict(sample)
    prediction = [{'name': 'utusmi', 'age': '15', 'sex': 'male'}, {'name': 'yamada', 'age': '15', 'sex': 'male'}, {'name': 'tanaka', 'age': '15', 'sex': 'male'}, {'name': 'utusmi', 'age': '13', 'sex': 'male'}, {'name': 'yamada', 'age': '13', 'sex': 'male'}, {'name': 'tanaka', 'age': '13', 'sex': 'male'}, {'name': 'utusmi', 'age': '15', 'sex': 'female'}, {'name': 'yamada', 'age': '15', 'sex': 'female'}, {'name': 'tanaka', 'age': '15', 'sex': 'female'}, {'name': 'utusmi', 'age': '13', 'sex': 'female'}, {'name': 'yamada', 'age': '13', 'sex': 'female'}, {'name': 'tanaka', 'age': '13', 'sex': 'female'}]
    assert result == prediction