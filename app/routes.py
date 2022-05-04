from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

# CREATE PLANET
@planets_bp.route("", methods = ["POST"])
def create_planet():
	request_body = request.get_json()
	new_planet = Planet(
		name = request_body["name"],
		description = request_body["description"],
		circumference = request_body["circumference"],
		length_of_year = request_body["length_of_year"]
	)

	db.session.add(new_planet)
	db.session.commit()

	return make_response(f"Planet {new_planet.name} has been successfully created", 201)

# GET ALL
@planets_bp.route("", methods = ["GET"])
def get_all_planets():
	planets_response = []
	planets = Planet.query.all()
	for planet in planets:
		planets_response.append(planet.to_json())
			
	return jsonify(planets_response)
    

# VALIDATE ID
def validate_planet(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"planet {id} is invalid"}, 400))

    planet = Planet.query.get(id)

    if not planet:
        abort(make_response({"message":f"planet {id} not found"}, 404))
    
    return planet

# GET ONE PLANET
@planets_bp.route("/<id>", methods = ["GET"])
def get_one_planet(id):
    planet = validate_planet(id)
    return jsonify(planet.to_json()), 200




	# {
	# 	"name": "Mercury"
	# 	"description": "made mostly of rocks"
	# 	"circumference": 9522
	# 	"length_of_year": 88
    # }

	
	# {
	# 	"name": Venus
	# 	"description": most like Earth
	# 	"circumference": 23617
	# 	"length_of_year":
    # }
	

	# {
	# 	"name": "Earth"
	# 	"description": "you are here"
	# 	"circumference": 24889
	# 	"length_of_year": 365
    # }


	# {
	# 	"name": "Mars"
	# 	"description": "the red planet"
	# 	"circumference": 13256
	# 	"length_of_year": 687
    # }


	# {
	# 	"name": "Jupiter",
	# 	"description": "largest planet",
	# 	"circumference": 278985,
	# 	"length_of_year": 4320
    # }


	# {
	# 	"name": "Saturn",
	# 	"description": "sun's bae with all 7 rings",
	# 	"circumference": 235185,
	# 	"length_of_year": 10620
    # }


	# {
	# 	"name": "Uranus",
	# 	"description": "can only be seen with a telescope",
	# 	"circumference": 99739,
	# 	"length_of_year": 30240
    # }


	# {
	# 	"name": "Neptune",
	# 	"description": "it is an intense blue color",
	# 	"circumference": 96645,
	# 	"length_of_year": 59400
    # }


	# {
	# 	"name": "Pluto",
	# 	"description": "no dwarf in my book",
	# 	"circumference": 7144,
	# 	"length_of_year": 88920
    # }
