import unittest
from parameterized import parameterized, parameterized_class
from ex2_roman.ex2_roman import roman
from nose.tools import assert_equal


@parameterized([
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (9, "IX")
])
def test_outside_class(number, expected):
    assert_equal(roman(number), expected)


@parameterized_class(('number', 'expected'), [
    (27, 'XXVII'),
    (48, 'XLVIII'),
    (49, 'XLIX'),
    (59, 'LIX'),
    (93, 'XCIII'),
    (141, 'CXLI'),
    (163, 'CLXIII')
])
class TestRoman(unittest.TestCase):
    def test_from_class(self):
        self.assertEqual(roman(self.number), self.expected)


class TestRoman2(unittest.TestCase):
    @parameterized.expand([
        (402, 'CDII'),
        (575, "DLXXV"),
        (911, 'CMXI'),
        (1024, 'MXXIV'),
        (3000, 'MMM')
    ])
    def test_from_method(self, number, expected):
        self.assertEqual(roman(number), expected)

    @parameterized.expand([
        ('greg', TypeError),
        (6000, ValueError)
    ])
    def test_from_method_error(self, number, expected):
        with self.assertRaises(expected):
            roman(number)


if __name__ == '__main__':
    unittest.main()
