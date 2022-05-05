
def test_get_all_planets_successfully(client):
	# Act
	response = client.get("/planets")
	# response has more than just json in it so we just want the json
	response_body = response.get_json()

	# Assert
	assert response.status_code == 200
	assert response_body == []  # comparing to empty list bc we are in our test database



def test_create_one_planet(client):
	# Act
    response = client.post("/planets", json={
        "name": "Goofy",
        "description": "goofy",
        "circumference": 1,
        "length_of_year": 1
    })
    response_body = response.get_json() 

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Goofy has been successfully created"

def test_get_one_planet_from_fixture_successfully(client, two_saved_planets):
    #act
    response = client.get("/planets/1")

    response_body = response.get_json()
    #assert
    assert response.status_code == 200
    assert response_body == {"name": "Mercury",
    "description": "made mostly of rocks",
    "circumference": 9522,
    "length_of_year": 88,
    "id": 1
    }
