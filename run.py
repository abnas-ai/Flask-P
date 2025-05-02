# from app import app, db
# from app.models import Employee

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] ='fd8ab5bd9d7f18715270fa3dd0005b645c7d7baae0967d0dbcd3d170caf70593'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abnas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Employee {self.name}>'

class Salary(db.Model):
    __tablename__ = 'salary'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    employee = db.relationship('Employee', backref='salaries')

    def __repr__(self):
        return f'<Salary {self.amount}>'
    
with app.app_context():
    db.create_all()
    
@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        department = request.form['department']
        salary = request.form['salary']

        new_employee = Employee(
            name=name,
            age=int(age),
            department=department,
            salary=float(salary)
        )
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_employee.html')

@app.route('/salaries')
def salaries():
    salaries = Salary.query.all()
    return render_template('salaries.html', salaries=salaries)

@app.route('/add_salary', methods=['GET', 'POST'])
def add_salary():
    employees = Employee.query.all()

    if request.method == 'POST':
        employee_id = request.form['employee_id']
        amount = request.form['amount']
        date = request.form['date']  # format: YYYY-MM-DD

        new_salary = Salary(
            employee_id=int(employee_id),
            amount=float(amount),
            date=datetime.strptime(date, '%Y-%m-%d')
        )
        db.session.add(new_salary)
        db.session.commit()
        return redirect(url_for('salaries'))

    return render_template('add_salary.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)