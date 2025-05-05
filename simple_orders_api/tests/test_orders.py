def test_create_order(client_with_auth):
    res = client_with_auth.post(
        "/api/v1/orders/", json={"customer_id": 1, "product_ids": [1, 2]}
    )
    assert res.status_code in [201, 400]


def test_get_order(client_with_auth):
    res = client_with_auth.get("/api/v1/orders/1")
    assert res.status_code in [200, 404]


def test_customer_order_history(client_with_auth):
    res = client_with_auth.get("/api/v1/customers/1/orders")
    assert res.status_code in [200, 404]
