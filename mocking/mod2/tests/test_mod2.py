from unittest import TestCase

from ..services import mod2_function


class TestMod2(TestCase):
    def test_mod2(self):
        expected = 'This is REAL mod2!'
        mod2_result = mod2_function()

        self.assertEqual(mod2_result, expected)
