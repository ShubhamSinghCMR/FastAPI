from datetime import datetime

from app.models import Order


def create_sample_orders(db):
    customers = db.query(Order.customer.property.mapper.class_).all()
    products = db.query(Order.products.property.mapper.class_).all()
    orders = []

    for i in range(min(len(customers), 2)):
        order_products = products[i * 2 : i * 2 + 2]
        total_cost = sum(p.price for p in order_products)

        order = Order(
            customer_id=customers[i].id,
            total_cost=total_cost,
            created_at=datetime.utcnow(),
        )
        order.products = order_products
        db.add(order)
        orders.append(order)

    db.commit()
    return orders
