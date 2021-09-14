import pytest


# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert 'h' in x
#     def test_two(self):
#         x = "hello"
#         assert hash(x,'check')
#     def test_three(self):
#         a = "hello"
#         b = "hello world"
#         assert a in b
#
#  if __name__ == '__main__':
#      pytest.main(['-q'], 'test_class.py')

# def func(x):
#     return x + 1
# def test_answer():
#     assert func(3) == 5
def test_a():
    print("test_a")
class Test_01:
    def test_one(self):
        print("开始执行 test_one 方法")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("开始执行 test_two 方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行 test_three 方法")
        a = 'hello'
        b = 'hello world'
        assert a in b
if __name__ == '__main__':
    pytest.main("-v -s Test_01")