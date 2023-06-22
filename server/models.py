from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    _tablename_ = 'zookeepers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    Animals = db.relationship('Animal', back_populates='zookeeper')


   

class Enclosure(db.Model):
    _tablename_ = 'enclosures'
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(50), nullable=False)
    open_to_visitors = db.Column(db.Boolean, default=False)
    Animals = db.relationship('Animal', back_populates='enclosure')
    



class Animal(db.Model):
    _tablename_ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))
    zookeeper= db.relationship('Zookeeper',back_populates='Animals')
    enclosure=db.relationship('Enclosure',back_populates='Animals')