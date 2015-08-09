from tsheets.model import Model


class User(Model):
    pass

User.add_field('id', 'int')
User.add_field('username', 'str')
User.add_field('email', 'str')
User.add_field('first_name', 'str')
User.add_field('last_name', 'str')
User.add_field('group_id', 'int')
User.add_field('manager_of_group_ids', ["int"])
User.add_field('employee_number', 'int')
User.add_field('salaried', 'bool')
User.add_field('exempt', 'bool')
User.add_field('payroll_id', 'str')
User.add_field('client_url', 'str')
User.add_field('mobile_number','str')
User.add_field('hire_date', 'date')
User.add_field('term_date', 'date')
User.add_field('last_active', 'datetime')
User.add_field('active', 'bool')
User.add_field('require_password_change', 'bool')
User.add_field('approved_to', 'date')
User.add_field('submitted_to', 'date')
User.add_field('last_modified', 'datetime')
User.add_field('created', 'datetime')
User.add_field('permissions', 'user_permissions_set')

