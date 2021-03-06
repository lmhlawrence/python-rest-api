from db import db

class StoreModel(db.Model):
    #setting up sqlalchemy
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90))

    #links the relationships of the store and items
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    #finds the item of the same name
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    #goes from object to inside the database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
