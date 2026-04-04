import json
from kafka import KafkaProducer
import sys

sys.path.append("src")
from generators.customer import CustomerGenerator

KAFKA_SERVER = "localhost:9092"
TOPIC_NAME = "finstream.customers"




if __name__ == "__main__":
    generator = CustomerGenerator()
    customer = generator.generate_customer()

    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

    print(f"Created customer info : {customer.first_name} {customer.last_name}")
    customer_json = customer.model_dump_json()
    customer_bytes = customer_json.encode("utf-8")

    producer.send(TOPIC_NAME, customer_bytes)
    producer.flush()
    print(f"Customer info sent to Kafka topic: {TOPIC_NAME}")