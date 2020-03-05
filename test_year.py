from unittest import TestCase

import year


class TestListdir(TestCase):

    def setUp(self):
        """Init"""

    def test_year(self):
        """Test for test_year"""
        self.assertFalse(year.leap_year(1900))
        self.assertTrue(year.leap_year(2000))

    def tearDown(self):
        """Finish"""
