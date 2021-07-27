import unittest

class TestTest:
    # https://docs.python.org/3/library/unittest.html
   
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ = "__main__":
    unittest.main()