from flask import Blueprint, request
from app.models import Employee, Position, Division, Job
from app import db

bp = Blueprint('bp', __name__)


@bp.route('/job/list', methods=['GET'])
def list_job():
    # job_all = db.session.query(Job).order_by(Job.date_of_employment).all()
    job = Employee.query.join(Job).order_by(Job.date_of_employment)
    if request.args.get('division_id'):
        job = job.filter(Job.division_id == request.args.get('division_id'))
    elif request.args.get('after_date'):
        job = job.filter(Job.date_of_employment > request.args.get('after_date'))
    job = job.all()
    result = [employee.to_dict() for employee in job]
    return result


@bp.route('/job/put', methods=['PUT'])
def put_job():
    dismissal = Job.query.get(request.args.get('id'))
    dismissal.date_of_dismissal = request.args.get('date_of_dismissal')
    db.session.add(dismissal)
    db.session.commit()
    return dismissal.to_dict()


@bp.route('/job/add', methods=['POST'])
def add_job():
    employee = Employee.query.get(request.args.get('employee_id'))
    position = Employee.query.get(request.args.get('position_id'))
    division = Employee.query.get(request.args.get('division_id'))
    job_list = {
        "employee_id": employee.id,
        "position_id": position.id,
        "division_id": division.id,
        "date_of_employment": request.args.get('date_of_employment'),
    }
    new_employee = Job(**job_list)
    db.session.add(new_employee)
    db.session.commit()
    return new_employee.to_dict()


@bp.route('/employee/add', methods=['POST'])
def add_employee():
    employee = Employee(**request.args)
    db.session.add(employee)
    db.session.commit()
    return employee.to_dict()


@bp.route('/employee/get', methods=['GET'])
def get_employee():
    employee = Employee.query.get(request.args.get('id'))
    return employee.to_dict()


@bp.route('/employee/delete', methods=['DELETE'])
def delete_employee():
    employee = Employee.query.get(request.args.get('id'))
    db.session.delete(employee)
    db.session.commit()
    return employee.to_dict()


@bp.route('/employee/put', methods=['PUT'])
def put_employee():
    employee = Employee.query.get(request.args.get('id'))
    if request.args.get('surname'):
        employee.surname = request.args.get('surname')
    if request.args.get('second_name'):
        employee.second_name = request.args.get('second_name')
    if request.args.get('firstname'):
        employee.firstname = request.args.get('firstname')
    if request.args.get('address'):
        employee.address = request.args.get('address')
    if request.args.get('date_of_birth'):
        employee.date_of_birth = request.args.get('date_of_birth')
    db.session.add(employee)
    db.session.commit()
    return employee.to_dict()


@bp.route('/position/add', methods=['POST'])
def add_position():
    position = Position(**request.args)
    db.session.add(position)
    db.session.commit()
    return position.to_dict()


@bp.route('/position/get', methods=['GET'])
def get_position():
    position = Position.query.get(request.args.get('id'))
    return position.to_dict()


@bp.route('/position/delete', methods=['DELETE'])
def delete_position():
    position = Position.query.get(request.args.get('id'))
    db.session.delete(position)
    db.session.commit()
    return position.to_dict()


@bp.route('/division/add', methods=['POST'])
def add_division():
    division = Division(**request.args)
    db.session.add(division)
    db.session.commit()
    return division.to_dict()


@bp.route('/division/get', methods=['GET'])
def get_division():
    division = Division.query.get(request.args.get('id'))
    return division.to_dict()


@bp.route('/division/delete', methods=['DELETE'])
def delete_division():
    division = Division.query.get(request.args.get('id'))
    db.session.delete(division)
    db.session.commit()
    return division.to_dict()

