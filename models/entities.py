from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class InitEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}".format(self.id, self.value)
