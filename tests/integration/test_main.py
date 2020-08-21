import io
import sys
import unittest
import unittest.mock

import transfer_message.__main__

class MainTestCase(unittest.TestCase):
    def test_main(self):
        message_ids_stdin = """A
B
C"""

        mocked_stdin = io.StringIO(message_ids_stdin)
        with unittest.mock.patch.object(sys, 'stdin', new=mocked_stdin) as stdin_mock:
            transfer_message.__main__.main([
                '--origin', 'foo',
                '--destination', 'bar'
                ])
