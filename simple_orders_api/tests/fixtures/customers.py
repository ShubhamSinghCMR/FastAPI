from app.models import Customer


def create_sample_customers(db):
    customers = [
        Customer(name=f"Customer {i}", email=f"cust{i}@test.com") for i in range(1, 4)
    ]
    db.add_all(customers)
    db.commit()
    return customers
