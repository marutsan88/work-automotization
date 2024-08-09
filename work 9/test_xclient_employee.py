import allure
from EmployeesApi import EmployeeApi
from CompanyTable import CompanyTable
from EmployeesTable import EmployeeTable


base_url = 'https://x-clients-be.onrender.com'
employee_api = EmployeeApi(base_url)

db_connection_string = ('postgresql://x_clients_db_3fmx_user:'
                        'mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@'
                        'dpg-cour99g21fec73bsgvug-a.oregon-postgres.'
                        'render.com/x_clients_db_3fmx')
company_table = CompanyTable(db_connection_string)
employee_table = EmployeeTable(db_connection_string)

# New company
name = 'NewCompany4'
description = 'My new company 4'

# New employee
id = 1
first_name = "Ilya4"
last_name = "Ilin"
middle_name = "Ilich"
email = "new@gmail.com"
employee_url = "url1.com"
phone = "+79998887766"
birthdate = "2000-06-07T08:06:30.137Z"
is_active = True


@allure.title('Get employee list')
@allure.description('Test get employee list by API')
@allure.feature('Employee')
@allure.severity(allure.severity_level.NORMAL)
def test_get_employee_list():
    # create new company in DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # create new employee in DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()

    # get employee list by API
    employee_list_api = employee_api.get_employee_list(new_company_id)

    # get employee list by DB
    employee_list_db = employee_table.get_company_employees(new_company_id)

    # delete new employee and new company from DB
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    with allure.step('Check new id is in the list'):
        assert employee_list_api[0]["id"] == new_employee_id, \
            "Employee's ID is not equal"
    with allure.step('Check that API list is equal DB list'):
        assert len(employee_list_api) == len(employee_list_db)


@allure.title('Create employee')
@allure.description('Test create employee by API')
@allure.feature('Employee')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_employee():
    # create new company in DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # create new employee by API
    new_employee = employee_api.add_employee(id, first_name, last_name,
                                             middle_name, new_company_id,
                                             email, employee_url, phone,
                                             birthdate, is_active)
    new_employee_id = new_employee["id"]

    # get employee from DB
    employee = employee_table.get_employee_by_id(new_employee_id)

    # delete new employee and new company from DB
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    with allure.step('Check that new employee was created in DB'):
        assert len(employee) == 1, "Employee was not created"


@allure.title('Get employee')
@allure.description('Test employee by API')
@allure.feature('Employee')
@allure.severity(allure.severity_level.NORMAL)
def test_get_employee():
    # create new company in DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # create new employee in DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()

    # get employee's info by API
    employee = employee_api.get_employee(new_employee_id)

    # delete new employee and new company from DB
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    with allure.step('Check that new id return from API'):
        assert employee["id"] == new_employee_id
    with allure.step('Check that new employee first name return from API'):
        assert employee["firstName"] == first_name
    with allure.step('Check response body length'):
        assert len(employee) == 12


@allure.title('Change employee by API')
@allure.description('Test change employee by API')
@allure.feature('Employee')
@allure.severity(allure.severity_level.NORMAL)
def test_change_employee_by_api():
    # create new company in DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # create new employee in DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()

    # patch employee by API
    new_email = "new_new@gmail.com"
    new_url = "url2.com"
    new_is_active = False
    patched_employee = employee_api.patch_employee(new_employee_id,
                                                   new_email, new_url,
                                                   new_is_active
                                                   )
    with allure.step('Check patched employee info from API'):
        assert patched_employee["id"] == new_employee_id
        assert patched_employee["email"] == new_email
        assert patched_employee["url"] == new_url
        assert patched_employee["isActive"] == new_is_active

    # get patched employee's info from DB
    employee = employee_table.get_employee_by_id(new_employee_id)

    # delete new employee and new company from DB
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    with allure.step('Check patched employee info from DB'):
        assert employee[0][0] == new_employee_id
        assert employee[0][8] == new_email
        assert employee[0][10] == new_url
        assert employee[0][1] == new_is_active


@allure.title('Change employee by DB')
@allure.description('Test change employee by DB')
@allure.feature('Employee')
@allure.severity(allure.severity_level.NORMAL)
def test_change_employee_by_db():
    # create new company in DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # create new employee in DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()

    # patch employee by DB
    new_email = "new_new@gmail.com"
    new_url = "url2.com"
    new_is_active = False
    employee_table.update(new_employee_id, new_email, new_url, new_is_active)

    # get employee's info by API
    employee = employee_api.get_employee(new_employee_id)

    with allure.step('Check patched employee info from API'):
        assert employee["id"] == new_employee_id
        assert employee["email"] == new_email
        assert employee["avatar_url"] == new_url
        assert employee["isActive"] == new_is_active