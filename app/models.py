from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
