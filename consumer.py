from json import loads
import os

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=os.environ.get("CONSUMER_GROUP_ID", "default"),
    value_deserializer=lambda x: loads(x.decode('utf-8')))

try:
    for message in consumer:
        print(message.value)

except Exception:
    consumer.close()
