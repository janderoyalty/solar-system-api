from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


# class Planet():
# 	def __init__(self, id, name, description, circumference, length_of_year):
# 		self.id = id
# 		self.name = name
# 		self.description = description
# 		self.circumference = circumference
# 		self.length_of_year = length_of_year

# 	def to_json(self): 
# 		return {
# 			"id" : self.id,
# 			"name" : self.name,
# 			"description" : self.description,
# 			"circumference" : self.circumference,
# 			"length_of_year" : self.length_of_year
# 		}

# planets = [
# 	Planet(1, "Mercury", "made mostly of rocks", 9522, 88), 
# 	Planet(2, "Venus", "most like Earth", 23617, 225), 
# 	Planet(3, "Earth", "you are here", 24889, 365),
# 	Planet(4, "Mars", "the red planet", 13256, 687),
# 	Planet(5, "Jupiter", "largest planet", 278985, 4320),
# 	Planet(6, "Saturn", "sun's bae with all 7 rings", 235185, 10620),
# 	Planet(7, "Uranus", "can only be seen with a telescope", 99739, 30240),
# 	Planet(8, "Neptune", "it is an intense blue color", 96645, 59400),
# 	Planet(9, "Pluto", "no dwarf in my book", 7144, 88920)
# ]

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

	return make_response(f"Planet {new_planet.name} has been successfully created", 201) #use make response when you want to return something that is not json

# GET ALL
@planets_bp.route("", methods = ["GET"])
def get_all_planets():
	planets_response = []
	planets = Planet.query.all()
	for planet in planets:
		# planets_response.append({
		# 	"id": planet.id,
		# 	"name": planet.name,
		# 	"description": planet.description,
		# 	"circumference": planet.circumference,
		# 	"length of year": planet.length_of_year
		# })
		planets_response.append(planet.to_json())
	return jsonify(planets_response) #need jsonify when returning list
    # planets_response = []
    # planets = Planet.query.all()
    # for planet in planets:
    #     planets_response.append(planet.to_json())

    # return jsonify(planets_response), 200

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
    # return jsonify({
	# 		"id": planet.id,
	# 		"name": planet.name,
	# 		"description": planet.description,
	# 		"circumference": planet.circumference,
	# 		"length of year": planet.length_of_year
	# })
    return jsonify(planet.to_json()), 200


	# {
	# 	name:
	# 	description:
	# 	circumference:
	# 	length_of_year:
    # }

@planets_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_planet(id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.circumference = request_body["circumference"]
    planet.length_of_year = request_body["length_of_year"]

    db.session.commit()

    return make_response(f"Planet #{id} succesffully updated"), 200


@planets_bp.route("/<id>", methods=["DELETE"])
def delete_one_planet(id):
    planet = validate_planet(id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{id} was successfully deleted"), 200
