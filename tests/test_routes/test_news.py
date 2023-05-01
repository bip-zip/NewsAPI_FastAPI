import json


def test_create_news(client):
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