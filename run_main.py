import pytest
if __name__ == '__main__':
    #-m=first 对优先级分类的引用
    pytest.main(['-s','-m=debug','--alluredir','./report/xml'])


