from cauldron import steptest
from unittest.mock import patch
from unittest.mock import MagicMock
import cauldron as cd

class MockResponse:

    def __init__(self):
        self.text = 'a,b,user_id\n1,2,3\n1,2,3'

class TestExampleDataPull(steptest.TestCase):
    """Test suite for my notebook"""

    @patch('requests.get') # modify the context of a function, substituting a fake function that we can control
    def test_simple_run(self, requests_get: MagicMock):
        """Should run notebook step without error""" # documentation run line starts with word Should

        requests_get.return_value = MockResponse()

        self.run_step("S01-Pull.py")
        self.assertIsNotNone(cd.shared.df) # should not be empty
        self.assertEqual(2 * 26, len(cd.shared.df)) # know the length
