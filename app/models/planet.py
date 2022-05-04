from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    circumference = db.Column(db.Integer)
    length_of_year= db.Column(db.Integer)
    
    def to_json(self):
        return {
			"id": self.id,
			"name": self.name,
			"description": self.description,
			"circumference": self.circumference,
			"length of year": self.length_of_year
		}