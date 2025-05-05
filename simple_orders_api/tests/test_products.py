def test_create_product(client_with_auth):
    res = client_with_auth.post(
        "/api/v1/products/", json={"name": "Gadget", "price": 49.99}
    )
    assert res.status_code == 201


def test_get_product(client_with_auth):
    res = client_with_auth.get("/api/v1/products/1")
    assert res.status_code in [200, 404]
