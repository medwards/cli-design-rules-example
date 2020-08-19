import unittest
import transfer_message.__main__

class MainTestCase(unittest.TestCase):
    def test_main(self):
        transfer_message.__main__.main(['1', '2', '3'])
