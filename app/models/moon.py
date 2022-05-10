from app import db

class Moon(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	size = db.Column(db.Integer)
	description = db.Column(db.String)
	surface_gravity = db.Column(db.Integer) #can be empty
	planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
	planet = db.relationship("Planet", back_populates = "moons")

	def to_json(self):
		return {
			"id": self.id,
			"size": self.size,
			"description": self.description,
			"surface_gravity": self.surface_gravity,
			"planet_id": self.planet_id
		}

	
