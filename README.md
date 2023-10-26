# PyTest

Project on pytest

Setup Configuration
-------------------

1. pip install pytest
2. pytest .\TestDir\TestFile.py

Non-Class based Tests:
----------------------

1. Within the _test(s) named file, pytest by default identifies all test methods based on name of function. If it has
   test in the name, it executes as test

Class based Tests:
-----------------
Methods provided synonymous to BeforeTest and AfterTest in TestNG

1. Setup_methodName
2. Teardown_methodName

Simple Setup and Teardown are static keywords so we cannot use them as test names
