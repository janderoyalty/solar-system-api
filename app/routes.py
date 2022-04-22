from crypt import methods
from flask import Blueprint, jsonify


class Planet():
	def __init__(self, id, name, description, circumference, length_of_year):
		self.id = id
		self.name = name
		self.description = description
		self.circumference = circumference
		self.length_of_year = length_of_year

planets = [
	Planet(1, "Mercury", "made mostly of rocks", 9522, 88), 
	Planet(2, "Venus", "most like Earth", 23617, 225), 
	Planet(3, "Earth", "you are here", 24889, 365),
	Planet(4, "Mars", "the red planet", 13256, 687),
	Planet(5, "Jupiter", "largest planet", 278985, 4320),
	Planet(6, "Saturn", "sun's bae with all 7 rings", 235185, 10620),
	Planet(7, "Uranus", "can only be seen with a telescope", 99739, 30240),
	Planet(8, "Neptune", "it is an intense blue color", 96645, 59400),
	Planet(9, "Pluto", "no dwarf in my book", 7144, 88920)
]

planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
	planets_response = []
	for planet in planets:
		planets_response.append({
			"id": planet.id,
			"name": planet.name,
			"description": planet.description,
			"circumference": planet.circumference,
			"length of year": planet.length_of_year
		})
	return jsonify(planets_response)




