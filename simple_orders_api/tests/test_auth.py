def test_login_logout_flow(client, auth_token):
    headers = {"Authorization": auth_token}

    res = client.get("/api/v1/customers/1", headers=headers)
    assert res.status_code in [200, 404]

    res = client.post("/api/v1/auth/logout", headers=headers)
    assert res.status_code == 200
    assert res.json()["message"] == "Successfully logged out"

    res = client.get("/api/v1/customers/1", headers=headers)
    assert res.status_code == 401
