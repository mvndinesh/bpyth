"""
from pageobjects.testcases.pyorghome import PythonHomePage
import unittest




def run_func():

    introduction = unittest.TestLoader().loadTestsFromTestCase(PythonHomePage)
    unittest.TextTestRunner(verbosity=3).run(introduction)


if __name__ == '__main__':
    run_func()
"""
