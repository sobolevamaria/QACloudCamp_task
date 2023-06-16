import requests
import os
import jsonschema

from schemas.post import post_schema

base_url = os.environ['BASE_URL']

class TestPostAPI:      
  def test_get_posts(self):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200

  def test_get_post(self):
    id = 1

    response = requests.get(f"{base_url}/posts/{id}")
    jsonschema.validate(instance=response.json(), schema=post_schema)
    assert response.status_code == 200
    
  def test_delete_post(self):
    body = self.get_post_body()
    response = requests.post(f"{base_url}/posts", json=body)
    assert response.status_code == 201
    jsonObj = response.json()
    id = jsonObj.get("id")

    response = requests.delete(f"{base_url}/posts/{id}")
    assert response.status_code == 200
    
  def test_post_post(self):
    body = self.get_post_body()
    
    response = requests.post(f"{base_url}/posts", json=body)
    jsonschema.validate(instance=response.json(), schema=post_schema)
    assert response.status_code == 201
    
  def get_post_body(self):
    body = {
      "title": "myTitle",
      "body": "myBody",
      "userId": 2
    }
    return body
