from unittest import TestCase
from unittest.mock import patch

from ..services import mod1_function


class TestMod1(TestCase):
    @patch('mod2.services.mod2_function', return_value='MOCKED!')
    def test_mod1(self, mock_mod2):
        expected = 'From _mod1_ I get this from _mod2_: [MOCKED!]'
        result = mod1_function()

        self.assertEqual(result, expected)
