from ..utils.database import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(25),nullable=False)
    email=db.Column(db.String(40),nullable=False,unique=True)
    password_hash=db.Column(db.Text(),nullable=False)
    books=db.relationship('Book',backref='added_by',lazy=True)


    def __repr__(self):
        return f"<User {self.username}>"
    
    @classmethod
    def get_by_email(cls,email):
        return cls.query.filter_by(email=email).first()



    def create_password_hash(self,password):
        self.password_hash=generate_password_hash(password)


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_by_username(cls,username):
        return cls.query.filter_by(username=username).first()


