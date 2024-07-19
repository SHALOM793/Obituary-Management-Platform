from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///obituary_platform.db"
db = SQLAlchemy(app)

class Obituary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    date_of_death = db.Column(db.Date, nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    submission_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    slug = db.Column(db.String(255), unique=True, nullable=False)

db.create_all()