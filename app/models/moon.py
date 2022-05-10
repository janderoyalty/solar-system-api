from app import db

class Moon(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	size = db.Column(db.Integer)
	description = db.Column(db.String)
	surface_gravity = db.Column(db.Integer) #can be empty
	planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
	planet = db.relationship("Planet", back_populates = "moons")



	
