from app import db

class Member(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(), index=True, unique=True)
	password = db.Column(db.String(50))
	name = db.Column(db.String(5))
	age = db.Column(db.String(5))
	tel = db.Column(db.String(20))
	email = db.Column(db.String(50))

	def __repr__(self):
		return '<Member %r>' % (self.nickname)

class Course(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(20))
	teacher_id = db.Colum(db.String(20))

	def __repr__(self):
		return '<Course id:{}, name:{}}>'.format(self.id, self.name)