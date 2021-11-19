import nsq

buf = []

def process_message(message):
    global buf
    message.enable_async()
    # cache the message for later processing
    buf.append(message)
    if len(buf) >= 3:
        for msg in buf:
            print(msg)
            msg.finish()
        buf = []
    else:
        print('deferring processing')

r = nsq.Reader(message_handler=process_message,
        lookupd_http_addresses=['http://127.0.0.1:4161'],
        topic='nsq_reader', channel='async', max_in_flight=9)
nsq.run()



import nsq

def handler(message):
    print(message)
    return True

r = nsq.Reader(message_handler=handler,
        lookupd_http_addresses=['http://127.0.0.1:4161'],
        topic='nsq_reader', channel='asdf', lookupd_poll_interval=15)
nsq.run()







