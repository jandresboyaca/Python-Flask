from flask import Flask, jsonify
from models import db, Parent, Child

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///init.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db.init_app(app)
db.create_all()


@app.route('/')
def test():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

with app.app_context():
    parent = Parent(value="test parent")
    child = Child(value="test child")
    parent.children.append(child)
    db.session.add(parent)
    db.session.commit()
    print(Parent.query.all())
    print(Parent.query.all()[0].children)
