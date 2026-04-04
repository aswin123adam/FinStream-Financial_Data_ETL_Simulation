import json
from kafka import KafkaProducer
import sys

sys.path.append("src")
from generators.transaction import TransactionGenerator

customer_ids = ["j1u4156ahc", "j1u4156ahd", "j1u4156ahe", "j1u4156ahf", "j1u4156ahg"]  # Sample customer IDs

KAFKA_SERVER = "localhost:9092"
TOPIC_NAME = "finstream.transactions"

if __name__ == "__main__":
    generator = TransactionGenerator(customer_ids)
    transaction = generator.generate_transaction()

    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

    print(f"Created transaction info : {transaction.transaction_id} for customer {transaction.customer_id}")
    transaction_json = transaction.model_dump_json()
    transaction_bytes = transaction_json.encode("utf-8")

    producer.send(TOPIC_NAME, transaction_bytes)
    producer.flush()
    print(f"Transaction info sent to Kafka topic: {TOPIC_NAME}")