import unittest
'''
given a string
when it is passed to the .upper() function
then the resultant will be upper case all chars 

given a string that has all letters in uppercase 
when it is tested with the .isupper() method
then the result is True

given a string that has at least one uppercase and at least one loiwercase char in it
when it is tested with the  .isupper() method 
then the result is False
'''
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()