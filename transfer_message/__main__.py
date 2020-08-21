import argparse
import os
import sys

import transfer_message

def main(args):
    if args is None:
        import sys
        args = sys.argv[1:]
    parser = create_argument_parser()
    args = parser.parse_args(args)
    message_ids = [line.strip() for line in sys.stdin.readlines()]
    origin = create_queue_wrapper(args.origin)
    destination = create_queue_wrapper(args.destination)
    transfer_message.transfer_message(origin, destination, message_ids)

def create_argument_parser():
    common_queue_help = 'Queue identifier in the form system:system_identifier, eg "aws:aws:us-east-1:123456". Supported systems: [aws, internal]'
    parser = argparse.ArgumentParser(
            prog='transfer_message',
            description='''
Transfer messages from one message queue to another. Origin and destination queues
are in different systems and have different native tooling, requiring this wrapper
to reliably transfer the messages between queues. A common use is getting messages
out of a dead letter queue into its intended destination after some event caused
valid messages to end up in the dead letter queue.
''')
    parser.add_argument('--origin', help=common_queue_help, metavar='QUEUE_ID', required=True)
    parser.add_argument('--destination', help=common_queue_help, metavar='QUEUE_ID', required=True)
    return parser

def create_queue_wrapper(queue_arg):
    system, queue = queue_arg.split(':', 1)
    if system == 'aws':
        client = External.AwsSQSClient()
    elif system == 'internal':
        client = External.InternalMessagesClient()
    else:
        raise Exception("Unexpected queue system in {}, expected aws or internal".format(queue_arg))
    return {'system': system,  # would be useful to retain this if clients have different interfaces
            'client': client,
            'queue': queue}

class External:
# This class represents external client dependencies of your tool
# All of these raise NotImplementedError to demonstrate easy mocking
    class AwsSQSClient:  # this would be a boto3 client in reality
        def get_message(self, queue, identifier):
            raise NotImplementedError()
        def write_message(self, queue, content):
            raise NotImplementedError()

    class InternalMessagesClient:  # some other client
        def get_message(self, queue, identifier):
            raise NotImplementedError()
        def write_message(self, queue, content):
            raise NotImplementedError()

if __name__ == "__main__":
    main()
