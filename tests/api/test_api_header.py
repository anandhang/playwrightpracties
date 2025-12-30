def test_api_get(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept":"application/json",
            "Authorization": "bearer YOUR_ACCESS_TOKEN",
            "X-Api-key":"reqres-free-v1"
        }
    )
    response = request.get("https://reqres.in/api/users?page=2&id=1")
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    #assert json_data["id"] == 1
    response.dispose()
    print("Test is completed successfully.")