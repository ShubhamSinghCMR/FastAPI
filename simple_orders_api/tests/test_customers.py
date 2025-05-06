def test_create_customer(client_with_auth):
    res = client_with_auth.post(
        "/api/v1/customers/", json={"name": "Jane Doe", "email": "jane@example.com"}
    )
    assert res.status_code == 201


def test_get_customer(client_with_auth):
    res = client_with_auth.get("/api/v1/customers/1")
    assert res.status_code in [200, 404]
