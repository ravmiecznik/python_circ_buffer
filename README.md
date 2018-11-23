# python_circ_buffer
# pytest -v --cov . --cov-report term --cov-report html --pep8
============================= test session starts ==============================
platform linux2 -- Python 2.7.15rc1, pytest-3.3.2, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python
cachedir: .cache
rootdir: /home/rafal/git/python_circ_buffer, inifile:
plugins: pylint-0.7.1, pep8-1.0.6, ordering-0.5, mccabe-0.1, cov-2.5.1
collecting ... collected 20 items

__init__.py PASSED                                                       [  5%]
circ_buffer.py PASSED                                                    [ 10%]
circ_buffer_test.py PASSED                                               [ 15%]
circ_buffer_test.py::test_circ_buffer_default_size PASSED                [ 20%]
circ_buffer_test.py::test_putchar PASSED                                 [ 25%]
circ_buffer_test.py::test_puts PASSED                                    [ 30%]
circ_buffer_test.py::test_put_combination PASSED                         [ 35%]
circ_buffer_test.py::test_get_from_empty_buffer PASSED                   [ 40%]
circ_buffer_test.py::test_available PASSED                               [ 45%]
circ_buffer_test.py::test_available_with_overflow PASSED                 [ 50%]
circ_buffer_test.py::test_gets_after_overflow PASSED                     [ 55%]
circ_buffer_test.py::test_flush PASSED                                   [ 60%]
circ_buffer_test.py::test_add_operator PASSED                            [ 65%]
circ_buffer_test.py::test_cbuffer_with_init_values PASSED                [ 70%]
circ_buffer_test.py::test_cbuffer_get_as_list_method PASSED              [ 75%]
circ_buffer_test.py::test_cbuffer_get_as_list_method_with_specifed_amount PASSED [ 80%]
circ_buffer_test.py::test_cbuffer_get_as_list_get_more_than_available PASSED [ 85%]
circ_buffer_test.py::test_iteration PASSED                               [ 90%]
circ_buffer_test.py::test_contains PASSED                                [ 95%]
circ_buffer_test.py::test_str PASSED                                     [100%]

-------- coverage: platform linux2, python 2.7.15-candidate-1 --------
Name                  Stmts   Miss  Cover
-----------------------------------------
__init__.py               1      0   100%
circ_buffer.py           91      2    98%
circ_buffer_test.py     107      7    93%
-----------------------------------------
TOTAL                   199      9    95%
Coverage HTML written to dir htmlcov


========================== 20 passed in 0.19 seconds ===========================
