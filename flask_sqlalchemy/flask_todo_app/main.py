from flask import Flask, request, jsonify
from model import db, Task

app = Flask(__name__)

# Use your working connection string here
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mssql+pyodbc://localhost\\SQLEXPRESS/ToDoDB?driver=ODBC+Driver+17+for+SQL+Server;'
    'Trusted_Connection=yes;Encrypt=no;'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'completed': t.completed} for t in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(title=data['title'], completed=False)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task added'}), 201

if __name__ == '__main__':
    app.run(debug=True)

