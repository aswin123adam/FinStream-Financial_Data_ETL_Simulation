from datetime import date, datetime
from enum import Enum
from uuid import uuid4
import random
from faker import Faker
from pydantic import BaseModel, Field

class CustomerSegment(str, Enum):
    MASS = "Mass"
    MASS_AFFLUENT = "Mass Affluent"
    AFFLUENT = "Affluent"
    HIGH_NET_WORTH = "High Net Worth"

class CreditTier(str, Enum):
    POOR = "Poor"
    FAIR = "Fair"
    GOOD = "Good"
    VERY_GOOD = "Very Good"
    EXCELLENT = "Excellent"

class Customer(BaseModel):
    customer_id: str = Field(default_factory=lambda: str(uuid4()))
    first_name: str
    last_name: str
    email: str
    phone: str
    date_of_birth: date
    city: str
    state: str
    country: str = "USA"  # Default value
    annual_income: float = Field(ge=0)  
    credit_score: int = Field(ge=300, le=850) 
    credit_tier: CreditTier
    customer_segment: CustomerSegment
    customer_since: date
    is_active: bool = True  # Default value
    created_at: datetime = Field(default_factory=datetime.utcnow)

if __name__ == "__main__":
    print(" Import checkpoint")

    # fake = Faker()
    # print(f"Fake name: {fake.name()}")
    # print(f"Fake address: {fake.address()}")
    # print(f"Fake email: {fake.email()}")
    # print(f"Fake city: {fake.city()}")

    # print("========Customer Segment ========")
    # for segment in CustomerSegment:
    #     print(f"Customer Segment: {segment.value}")
    
    # print("========Credit Tier ========")
    # for tier in CreditTier:
    #     print(f"Credit Tier: {tier.value}")

    # mySegment = random.choice(list(CustomerSegment))
    # myTier = random.choice(list(CreditTier))

    # print(f"Randomly selected Customer Segment: {mySegment.value}")
    # print(f"Randomly selected Credit Tier: {myTier.value}")

    print("=" * 60)
    print("Pydantic Check")
    print("=" * 60)
    
    try:
        customer = Customer(
            first_name="Aswin",
            last_name="Muthusamy",
            email="aswinmuthusamy98@gmail.com",
            phone="123-456-7890",
            date_of_birth=date(1998, 1, 14),
            city="Dublin",
            state="Leinster",
            country="Ireland",
            annual_income=82000.00,
            credit_score=825,
            credit_tier=CreditTier.EXCELLENT,
            customer_segment=CustomerSegment.AFFLUENT,
            customer_since=date(2020, 5, 20)
        )

        print("========== CUSTOMER INSTANCE CREATED SUCCESSFULLY ==========")
        print(f"customer_name: {customer.first_name} {customer.last_name}")
        print(f"credit_score: {customer.credit_score}")

    except Exception as e:
        print("Error creating Customer instance: Credit Score is not valid.")
        print(e)