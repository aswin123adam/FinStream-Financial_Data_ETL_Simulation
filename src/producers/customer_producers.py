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

    print(f"Generated Customer:\nFull Name: {customer.first_name} {customer.last_name},\nemail: {customer.email} ,\nphone: {customer.phone},\nDOB: {customer.date_of_birth},\ncity: {customer.city},\nstate: {customer.state},\ncountry: {customer.country},\ncustomer_since: {customer.customer_since},\nGenerated Customer: {customer.customer_segment.value} ,\nincome: {customer.annual_income:,.2f},\ncredit_score: {customer.credit_score}")