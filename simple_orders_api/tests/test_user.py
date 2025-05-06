def test_register_user(client):
    user = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "password123",
    }
    res = client.post("/api/v1/auth/register", json=user)
    assert res.status_code in [200, 201]


def test_duplicate_user_registration(client):
    user = {
        "username": "dupeuser",
        "email": "dupeuser@example.com",
        "password": "pass123",
    }
    client.post("/api/v1/auth/register", json=user)
    res = client.post("/api/v1/auth/register", json=user)
    assert res.status_code == 400


def test_login_invalid_credentials(client):
    res = client.post(
        "/api/v1/auth/login", data={"username": "nosuchuser", "password": "wrong"}
    )
    assert res.status_code == 401
