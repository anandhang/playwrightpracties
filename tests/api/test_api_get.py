
def test_api_get(playwright):
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/posts/1", header={"Accept":"aplication/json"})
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    assert json_data["id"] == 1
    response.dispose()
    print("Test is completed successfully.")