import logging

from kafka import KafkaConsumer

server = ["kafka01.kvm.lan:9092"]
topic = "test"


#logging.basicConfig(level=logging.DEBUG)


consumer = KafkaConsumer(
    topic,
    bootstrap_servers=server,
    api_version=(0, 10, 1)
)

for msg in consumer:
    print(msg)
