from flask import Flask
from flask_sqlalchemy import SQLAlchemy

print("✅ Import successful!")

app = Flask(__name__)
print("🔍 app object created:", app)
print("📦 app type is:", type(app))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # using SQLite for now
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    print("⚙️ Creating tables...")
    db.create_all()

@app.route('/')
def home():
    return '✅ Flask is working!'

if __name__ == '__main__':
    app.run(debug=True)




