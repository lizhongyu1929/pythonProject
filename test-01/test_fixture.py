import pytest


def test_case1(login):
    print("test_casel,要登录")
    pass

def test_case2():
    print("test_case2,不需要登录")
    pass

if __name__ == '__main__':
    pytest.main()