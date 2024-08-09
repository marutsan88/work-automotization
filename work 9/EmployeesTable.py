import allure
from sqlalchemy import create_engine
from sqlalchemy.sql import text


class EmployeeTable:
    scripts = {
        "delete employee": text("DELETE FROM employee "
                                "WHERE id = :new_employee_id"),
        "get company's employees": text("SELECT * FROM employee "
                                        "WHERE company_id = :company_id"),
        "get employee by id": text("SELECT * FROM employee "
                                   "WHERE id = :employee_id"),
        "get max id": text("SELECT MAX(id) FROM employee"),
        "insert new": text("INSERT INTO employee(first_name, last_name, "
                           "phone, company_id, is_active) "
                           "VALUES (:first_name, :last_name, :phone, "
                           ":company_id, :is_active)"),
        "update employee": text("UPDATE employee "
                                "SET email = :new_email, "
                                "avatar_url = :new_url, "
                                "is_active = :new_is_active "
                                "WHERE id = :new_employee_id")
    }

    def __init__(self, db_connection_string: str) -> None:
        self.db = create_engine(db_connection_string)

    @allure.step('Create new employee in DB')
    def create(self, first_name: str, last_name: str, phone: str,
               company_id: int, is_active: bool) -> None:
        '''
        Create new employee
        '''
        new_employee = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "company_id": company_id,
            "is_active": is_active
        }
        self.db.execute(self.scripts["insert new"], new_employee)

    @allure.step('Delete employee from DB by id')
    def delete(self, id: int) -> None:
        '''
        Delete employee by id
        '''
        self.db.execute(self.scripts["delete employee"], new_employee_id=id)

    @allure.step('Get employees list from DB')
    def get_company_employees(self, new_company_id: int) -> list:
        '''
        Get company's employees
        '''
        return self.db.execute(self.scripts["get company's employees"],
                               company_id=new_company_id).fetchall()

    @allure.step('Get employee from DB by id')
    def get_employee_by_id(self, id: int) -> list:
        '''
        Get employee by id
        '''
        return self.db.execute(self.scripts["get employee by id"],
                               employee_id=id).fetchall()

    @allure.step('Get max employee id from DB')
    def get_max_id(self) -> int:
        '''
        Get max employee id (last created)
        '''
        return self.db.execute(self.scripts["get max id"]).fetchall()[0][0]

    @allure.step('Update employee in DB')
    def update(self, id: int, email: str, url: str, is_active: bool) -> None:
        '''
        Update employee
        '''
        self.db.execute(self.scripts["update employee"], new_email=email,
                        new_url=url, new_is_active=is_active,
                        new_employee_id=id)