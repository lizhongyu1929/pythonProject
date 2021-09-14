# import unittest
# import HTMLTestRunner


# import unittest
# import HTMLTestRunner

# def test_one():
#     print('我是方法一')
#     x = "this"
# def test_two():
#     print('我是方法二')
#     y = 5
#     assert y > 6


import pytest
import yaml


class TestData:
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def test_data(self,a,b):
        print(a+b)