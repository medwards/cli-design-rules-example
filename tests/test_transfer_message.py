import unittest
import unittest.mock

import transfer_message

class TransferMessageTestCase(unittest.TestCase):
    def test_transfer_message(self):
        origin = {'system': 'aws',
                  'client': unittest.mock.Mock(),
                  'queue': 'aws:us-east-1:123456'}
        origin['client'].get_message.return_value = 'MESSAGE'
        destination = {'system': 'internal',
                       'client': unittest.mock.Mock(),
                       'queue': 'internal_id'}
        message_ids = list('a')

        transfer_message.transfer_message(origin, destination, message_ids)

        origin['client'].get_message.assert_called_with('aws:us-east-1:123456', 'a')
        destination['client'].write_message.assert_called_with('internal_id', 'MESSAGE')
