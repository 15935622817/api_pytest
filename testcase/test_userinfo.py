# import pytest
# class Test_class():
#     @pytest.fixture()
#     def  my_fixture(this):
#         print("用户信息模块：用户初始化操作")
#         yield
#         print("用户推fffffff出")
#
#     @pytest.mark.first
#     @pytest.mark.usefixtures("my_fixture")
#     def test_first(this):
#      #   assert 1==2
#          print('用户信息模块：第一个测试用例')
#          #assert 1!= 2
#     @pytest.mark.usefixtures("my_fixture") #在执行test_scond时先执行my_fixture
#     def test_second(this):
#         #   assert 1==2
#         print('用户信息模块：第二个测试用例')
#         # assert 2 == 2
#         # assert 'a' in 'abc'
#     @pytest.mark.usefixtures("my_fixture")
#     def test_three(this):
#         #   assert 1==2
#         print('用户信息模块：第三个测试用例')
#         # assert 'a' not in 'b'
#     def test_four(this):
#         #   assert 1==2
#         print('用户信息模块：第四个测试用例')
#         dlist=[1,2,3,4]
#         # assert 1 in dlist
#     def test_five(this):
#         #   assert 1==2
#         print('用户信息模块：第五个测试用例')
#     # assert assValue(3,5)
# # def assValue(a,b):
# #     #   assert 1==2
# #     if  a>b:
# #         return True
# #     else:
# #         return False
#
# # if __name__ == '__main__':
# #     pytest.main(['-s'])