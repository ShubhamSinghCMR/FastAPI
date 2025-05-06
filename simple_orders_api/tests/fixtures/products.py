from app.models import Product


def create_sample_products(db):
    products = [Product(name=f"Product {i}", price=10.0 * i) for i in range(1, 6)]
    db.add_all(products)
    db.commit()
    return products
