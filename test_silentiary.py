"""Unit tests for silentiary.py"""
import unittest

import silentiary


class TestSilentiary(unittest.TestCase):

    def test_something(self):
        self.assertTrue('FOO'.isupper())


if __name__ == '__main__':
    import os
    import shutil

    TEST_HOME = os.path.expanduser('~/.silentiary_test/')
    silentiary.HOME = TEST_HOME
    if os.path.isdir(TEST_HOME):
        print("unclean test directory: "+TEST_HOME)
        os._exit(1)

    #generate a test key...

    #initialize with the new key

    #run the test suite
    unittest.main()

    #delete the test key, and testing directory
    shutil.rmtree(TEST_HOME)
