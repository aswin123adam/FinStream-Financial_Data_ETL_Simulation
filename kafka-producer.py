from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

message = {
    'username' : 'Aswin',
    'message' : 'Hello, Kafka!',
    'customer_id': '12345',
    'action': 'first kafka message'
}

producer.send('test-topic', value=message)
producer.flush()

print("Message sent to Kafka topic 'test-topic'")
print("Message content:", message)