from flask import Flask
from models import db, InitEntity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///init.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db.init_app(app)
db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

with app.app_context():
    i = InitEntity(id=2, value="test")
    db.session.add(i)
    db.session.commit()
    print(InitEntity.query.all())
