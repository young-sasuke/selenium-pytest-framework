'''
markers
there are two markers
custom markers
inbuild markers

'''
from pickle import FALSE

#
# import pytest
#
#
# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_login():
#     print("login execution")
# @pytest.mark.smoke
# def test_reg():
#     print("reg execution")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup execution")
#
# @pytest.mark.regression
# def test_logout():
#     print("test logout")
#
#

# @pytest.mark.bhaskar

# pytest test_markers.py -vs -m=bhaskar


# pytest test_markers.py -vs -m="sanity and smoke"  -->0 because there is and act like a logical operator
# pytest test_markers.py -vs -m="sanity or smoke"   --> 3  it also act as the logical or
# pytest test_markers.py -vs -m="not sanity" -->2 selected
# to groupp the test case in two grouop---->
# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_login():
#     print("login execution")




'''
now inbuild markers
first one is skip
skip-->if you want to skip the execution of the test case then you will go for the skip markers
'''


import pytest




# @pytest.mark.skip
# def test_login():
#     print("login execution")
#
# def test_reg():
#     print("reg execution")
#
#
# def test_signup():
#     print("signup execution")
#
#
# def test_logout():
#     print("test logout")
#
#
#
# (.venv) PS C:\Users\KIIT\PycharmProjects\selenium_project\training> pytest test_markers.py -vs
# =============================================================================== test session starts ===============================================================================
# platform win32 -- Python 3.12.2, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\KIIT\PycharmProjects\selenium_project\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.2', 'Platform': 'Windows-11-10.0.26200-SP0', 'Packages': {'pytest': '9.0.2', 'pluggy': '1.6.0'}, 'Plugins': {'html': '4.2.0', 'metadata': '3.1.1'}, 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk-21'}
# rootdir: C:\Users\KIIT\PycharmProjects\selenium_project\training
# plugins: html-4.2.0, metadata-3.1.1
# collected 4 items
#
# test_markers.py::test_login SKIPPED (unconditional skip)
# test_markers.py::test_reg reg execution
# PASSED
# test_markers.py::test_signup signup execution
# PASSED
# test_markers.py::test_logout test logout
# PASSED

#
# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print("login execution")
#
#     def test_reg(self):
#         print("reg execution")
#
#     def test_signup(self):
#         print("signup execution")
#
#     def test_logout(self):
#         print("test logout")
#
#
#

# plugins: html-4.2.0, metadata-3.1.1
# collected 4 items
#
# test_markers.py::TestSample::test_login SKIPPED (unconditional skip)
# test_markers.py::TestSample::test_reg SKIPPED (unconditional skip)
# test_markers.py::TestSample::test_signup SKIPPED (unconditional skip)
# test_markers.py::TestSample::test_logout SKIPPED (unconditional skip)
#


'''
inbuild marker
skipif    -->if the condition is true thenit will stop the execution else it execute the test case
@pytest.mark.skipif(True,reason="login already happen")
if you not pass the condition then it will not  execute  by default it tale the true
if you not give the reason it will give error to specify the reason it is mendatory condition
'''

# @pytest.mark.skipif(True,reason="login already happen")
# def test_login(self):
#     print("login execution")



# collected
# 1
# item
#
# test_markers.py::test_login
# SKIPPED(login
# already
# happen)

'''
xfail--> if you want or expect a specific test case to not execute fine or expecting a failure from a testcase 
output--> xfail if the testcase fail
'''
#
# @pytest.mark.xfail
# def test_login():
#     raise Exception
#
# # plugins: html-4.2.0, metadata-3.1.1
# # collected 1 item
# #
# # test_markers.py::test_login XFAIL


#
# @pytest.mark.xfail
# def test_login():
#     print("login")
#
# #
# # plugins: html-4.2.0, metadata-3.1.1
# # collected 1 item
# #
# # test_markers.py::test_login login
# # XPASS
# #
# # ===================


'''
parameterize
when you want to pass the parameter in the test function and you  do not those to be a fixture you want actual normal parameter
'''

# @pytest.mark.parametrize("a,b",[(10,10)])
# def test_add(a,b):
#     print(a+b)
#
# # collected 1 item
# #
# # test_markers.py::test_add[10-10] 20
# # PASSED



# ("a,b",[[10,10]])--> it find at the 0the index of the list or outer lise the  on zero index it get [10.20]
# se can do any combination of list and tuple

#
# @pytest.mark.parametrize("a,b",[(10,10),(1,2),(5,6),(20,10)])
# def test_add(a,b):
#     print(a+b)
#
# # it will execute for the every test case like every tuple , each tuple will be consider as a indivisual test case
# # collected 4 items
# #
# # test_markers.py::test_add[10-10] 20
# # PASSED
# # test_markers.py::test_add[1-2] 3
# # PASSED
# # test_markers.py::test_add[5-6] 11
# # PASSED
# # test_markers.py::test_add[20-10] 30
# # PASSED







