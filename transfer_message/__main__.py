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
    transfer_message.transfer_message(args.origin, args.destination, message_ids)

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

if __name__ == "__main__":
    main()
