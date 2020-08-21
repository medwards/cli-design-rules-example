def transfer_message(origin, destination, message_ids):
    for message_id in message_ids:
        message = origin['client'].get_message(origin['queue'], message_id)
        # maybe transform the message here somehow
        destination['client'].write_message(destination['queue'], message)
