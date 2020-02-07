from json import dumps
import time
import os

producer_name = os.environ.get("PRODUCER_GROUP_ID", "default")
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['kafka:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))
try:
    while True:
        producer.send("test", value={"sender": producer_name, "hello": "producer"})
        time.sleep(4)

except:
    print(f"{producer_name} says good bye")
    producer.close()
