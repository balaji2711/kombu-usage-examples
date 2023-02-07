from kombu import Connection, Exchange, Queue, Consumer

url = 'localhost'
userid = 'guest'
password = 'guest'

conn = Connection(hostname=url, userid=userid, password=password)
exchange = Exchange('locust-events', type='direct', durable=True)
queue = Queue(name='locust-queue 1', exchange=exchange, routing_key='python1', queue_arguments={"x-queue-type": "quorum"})


def process_message(body, message):
    print("Received body - {}".format(body))
    print("Size of the message - {}".format(len(body)))
    message.ack()


with Consumer(conn, queues=queue, callbacks=[process_message], accept=['application/json']):
    while True:
        print('Receiving...')
        conn.drain_events()
