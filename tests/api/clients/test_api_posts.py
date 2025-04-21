import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_get_all_posts():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_post():
    response = requests.get(f"{BASE_URL}/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/9999")
    assert response.status_code in [404, 200]

def test_create_post_valid():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201

def test_create_post_missing_fields():
    payload = {"title": "foo"}
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201

def test_create_post_invalid_data():
    payload = "this is not json"
    response = requests.post(BASE_URL, data=payload)
    assert response.status_code in [400, 500, 201]

def test_patch_post_valid():
    payload = {"title": "updated"}
    response = requests.patch(f"{BASE_URL}/1", json=payload)
    assert response.status_code == 200

def test_patch_post_invalid_id():
    payload = {"title": "nope"}
    response = requests.patch(f"{BASE_URL}/9999", json=payload)
    assert response.status_code in [404, 200]

def test_delete_existing_post():
    response = requests.delete(f"{BASE_URL}/1")
    assert response.status_code == 200

def test_delete_nonexistent_post():
    response = requests.delete(f"{BASE_URL}/9999")
    assert response.status_code in [404, 200]

def test_post_invalid_method():
    response = requests.put(BASE_URL)
    assert response.status_code in [404, 405]

def test_post_large_payload():
    big_data = {"title": "a" * 10000, "body": "b" * 10000, "userId": 1}
    response = requests.post(BASE_URL, json=big_data)
    assert response.status_code in [201, 413]

def test_invalid_auth_token():
    headers = {"Authorization": "Bearer faketoken"}
    response = requests.get(BASE_URL, headers=headers)
    assert response.status_code in [200, 401]