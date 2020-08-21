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
        with unittest.mock.patch.object(sys, 'stdin', new=mocked_stdin) as stdin_mock, unittest.mock.patch.object(transfer_message.__main__.External, 'AwsSQSClient') as aws_mock, unittest.mock.patch.object(transfer_message.__main__.External, 'InternalMessagesClient') as internal_mock:
            # TODO: need to properly mock client creation and return values here
            transfer_message.__main__.main([
                '--origin', 'aws:aws:us-east-1:123456',
                '--destination', 'internal:internal_id'
                ])
            # TODO: then have to reach through the mocks to do some verification
