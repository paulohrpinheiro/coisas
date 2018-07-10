from unittest import TestCase

from ..services import mod1_function


class TestMod1(TestCase):
    def test_mod1(self):
        expected = 'I don\'t remember'
        result = mod1_function()

        self.assertEqual(result, expected)
