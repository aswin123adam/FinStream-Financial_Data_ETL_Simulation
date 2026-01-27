from datetime import datetime
from enum import Enum
from uuid import uuid4
import random
from faker import Faker
from pydantic import BaseModel, Field

if __name__ == "__main__":
    print(" Import checkpoint")

    fake = Faker()
    print(f"Fake name: {fake.name()}")
    print(f"Fake address: {fake.address()}")
    print(f"Fake email: {fake.email()}")
    print(f"Fake city: {fake.city()}")