import logging

from kafka import KafkaProducer


logging.basicConfig(level=logging.DEBUG)


server = "kafka01.kvm.lan:9092"
topic = "test"
msg = b"my_message"

producer = KafkaProducer(
    bootstrap_servers=server,
    api_version=(0, 10, 1),
)

producer.send(topic, msg)

producer.flush()
