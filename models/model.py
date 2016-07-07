from application import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            email=self.email
        )
