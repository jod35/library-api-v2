from ..utils.database import db
import datetime

class Book(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(45),nullable=False)
    author=db.Column(db.String(25),nullable=False)
    isbn=db.Column(db.Text(),nullable=False)
    user_id=db.Column(db.Integer(),db.ForeignKey('user.id'))
    date_added=db.Column(db.DateTime(),default=datetime.datetime.utcnow)


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
    def get_by_title(cls,title):
        return cls.query.filter_by(title=title).first()

