from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(128))
    children = db.relationship('Child', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return "{}-{}".format(self.id, self.value)


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(128))
    parent = db.Column(db.Integer, db.ForeignKey('parent.id'))
    __table_args_ = (db.UniqueConstraint('parent', 'value', name='fk'))

    def __repr__(self):
        return "{}-{}".format(self.id, self.value)
