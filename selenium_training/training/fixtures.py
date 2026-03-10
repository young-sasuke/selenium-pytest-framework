# def outer(fun):
#     def wrapper(*args,**kwargs):
#         print("good morning")
#         fun(*args,**kwargs)
#     return wrapper
#
#
# @outer
# def add(a,b):
#     print(a+b)
#
# add(10,20)
import pytest


@pytest.fixture(autouse=True,scope="module")
def greet():
    print("good morning")    #setup
    yield
    print("good evening")    #teardown

# now greet is a fixture function,test function only take fixture as a parameter
# the operation before yield  execute befor the test fn and after yield execute aftert he fn
# if you dot he autouse =true then it will autometically apply ti the all fn without passing as argument ex:@pytest.fixture(autouse=True)
# scope="class" then decorater will apply class wise
# scope="module" then decorator will apply on module



# def test_login(greet):
#     print("login")
#
#
# def test_logout(greet):
#     print("logout")
#
# def test_signup():
#     print("singup")



class TestSample:
    def test_login(self):
        print("login")

    def test_logout(self):
        print("logout")

    def test_signup(self):
        print("singup")


class TestExample:
    def test_gmail(self):
        print("gmail")
    def test_yahoo(self):
        print("yahoo")

#



