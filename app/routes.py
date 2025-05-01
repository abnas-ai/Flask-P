
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Employee, Salary
from datetime import datetime

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



