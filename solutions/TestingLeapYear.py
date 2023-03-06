import unittest
from TDD_ex01_leap_year_sln import *
'''
given a user input 
when it is cast to int
then it is successful 

given a user input 
when it fails to be cast to int
then report to the user AND close the application

'''
class TestLeapYearMethods(unittest.TestCase):

    def test_cast_passes(self):
        self.assertTrue("valid year" in Leaper.response(2000).lower())

    def test_cast_fails(self):
        self.assertTrue("not a valid year" in Leaper.response("stuff").lower())

    def test_for_div_4(self):
        self.assertTrue(Leaper._divisible_by_4(2000))
        self.assertFalse(Leaper._divisible_by_4(2001))

    def test_for_div_100(self):
        self.assertTrue(Leaper._divisible_by_100(2000))
        self.assertFalse(Leaper._divisible_by_100(2001))

    def test_for_div_400(self):
        self.assertTrue(Leaper._divisible_by_400(2000))
        self.assertFalse(Leaper._divisible_by_400(2001))

    def test_leap_year_rules(self):
        self.assertIn("This is a leap year", Leaper.response(2000))
        self.assertIn("This is not a leap year", Leaper.response(2001))
        self.assertIn("This is not a leap year", Leaper.response(3000))


'''
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
'''
if __name__ == '__main__':
    unittest.main()