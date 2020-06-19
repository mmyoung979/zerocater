# Django imports
from django.test import TestCase

# Python imports
from datetime import datetime

# Project imports
from restaurants.utils import is_vendor_available


# Should always work anywhere
class SanityTestCase(TestCase):
    def test_exceptions_get_caught(self):
        self.assertEqual(2 + 2, 4)
        with self.assertRaises(ZeroDivisionError):
            1 / 0


class VendorTestCase(TestCase):

    @staticmethod
    def time(x):
        return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

    def test_unavailable_vendor(self):
        self.assertEqual(is_vendor_available(1, self.time("2017-01-01 14:30:00")), False)
        self.assertEqual(is_vendor_available(1, self.time("2017-01-02 14:30:00")), True)
        self.assertEqual(is_vendor_available(2, self.time("2017-01-01 13:30:00")), True)

    def test_vendor_id_existence(self):
        with self.assertRaises(ValueError):
            is_vendor_available(0, self.time("2017-01-02 14:30:00"))
            is_vendor_available(3, self.time("2017-01-02 14:30:00"))
