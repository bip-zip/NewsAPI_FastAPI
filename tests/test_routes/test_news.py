import json


def test_create_news(client, normal_user_token_headers):
    data = {
        "title": "SDE super",
        "thumbnail": "python.jpg",
        "description": "All in all is all we are",
        "date_posted": "2022-03-20"
        }
    response = client.post("/news/create-news/",data = json.dumps(data))
    assert response.status_code == 200 
    assert response.json()["title"] == "SDE super"
    assert response.json()["description"] == "All in all is all we are"


def test_read_news(client):    
    data = {
        "title": "okok",
        "thumbnail": "okok.jpg",
        "description": "all in all is all we are",
        "date_posted": "2023-05-01",
        "is_approved": False
        }
    response = client.post("/news/create-news/",data=json.dumps(data))

    response = client.get("/news/get/1/")
    assert response.status_code == 200
    assert response.json()['title'] == "okok"

def test_read_all_news(client):    
    data = {
        "title": "okok",
        "thumbnail": "okok.jpg",
        "description": "all in all is all we are",
        "date_posted": "2023-05-01",
        "is_approved": False
        }
    response = client.post("/news/create-news/",data=json.dumps(data))
    response = client.post("/news/create-news/",data=json.dumps(data))

    response = client.get("/news/all/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]

def test_update_a_news(client):
    data = {
        "title": "okok",
        "thumbnail": "okok.jpg",
        "description": "all in all is all we are",
        "date_posted": "2023-05-01",
        "is_approved": False
        }
    client.post("/news/create-news/",data=json.dumps(data))
    data["title"] = "test new title"
    response = client.put("/news/update/1",data=json.dumps(data))
    assert response.json()["msg"] == "Successfully updated data."

def test_delete_a_news(client):
    data = {
        "title": "okok",
        "thumbnail": "okok.jpg",
        "description": "all in all is all we are",
        "date_posted": "2023-05-01",
        "is_approved": False
        }
    client.post("/news/create-news/",data=json.dumps(data))
    data["title"] = "test new title"
    response = client.put("/news/delete/1",data=json.dumps(data))
    assert response.json()["msg"] == "Successfully deleted data."