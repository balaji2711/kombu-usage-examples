from kombu import Connection, Exchange, Queue
import time

url = 'localhost'
userid = 'guest'
password = 'guest'

conn = Connection(hostname=url, userid=userid, password=password)
producer_channel = conn.channel()
data = {'name': 'Automation'}
exchange = Exchange('locust-events', type='direct', durable=True)
producer = conn.Producer(serializer='json')
queue = Queue(name='locust-queue 1', exchange=exchange, routing_key='python1', queue_arguments={"x-queue-type": "quorum"})
while True:
    print('Sending...')
    producer.publish(data, exchange=exchange, routing_key='python1', declare=[queue])
    time.sleep(5)
