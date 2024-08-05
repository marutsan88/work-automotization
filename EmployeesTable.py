from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeesTable:
    __scripts = {
        "insert company": text("insert into company (\"name\", \"description\") values (:new_name, :new_descr)"),
        "get max id company": text("select MAX(id) from company"),
        "select": text("select * from employee where company_id = :id"),
        "insert new employee": text("insert into employee (first_name, last_name, middle_name, phone, email, birthdate, avatar_url, is_active, company_id) values (:first_name, :last_name, :middle_name, :phone, :email, :birthdate, :avatar_url, :is_active, :company_id)"),
        "get max id empl": text("select MAX(id) from employee"),
        'edited employee': text("update employee set last_name = :new_lastName, email = :new_email, url = :new_url, phone = :new_phone, isActive = :new_isActive where id = :employeeId"),
        'delete id employee': text("delete from employee where id = :max_id_empl"),
        "delete by id": text("delete from company where id = :max_id")
         }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    # БД.Создать организацию с названием 
    def create_company_db(self, name: str, description: str):
        query = self.__db.execute(self.__scripts["insert company"], new_name = name, new_descr = description)
        

    # БД. Получить максимальный id организации
    def get_max_id_company(self, id: int):
        query = self.__db.execute(self.__scripts["get max id company"], max_id = id)
        return query.fetchall()[0][0]

    # БД. Получить список сотрудников организации {company_id}
    def get_emploees_db(self, company_id: int):
        query = self.__db.execute(self.__scripts["select"], id = company_id)
        return query.fetchall()

    # БД. Удалить организацию по {id}
    def delete(self, id: int):
        query = self.__db.execute(self.__scripts["delete by id"], max_id = id)


    # БД.Создать организацию с названием {first_name,last_name,middle_name,phone,email,birthdate,avatar_url,company_id,is_active}
    def create_employee_db(self, first_name: str, last_name: str, middle_name: str, phone: int, email: str, birthdate: bool, avatar_url: str, company_id: int, is_active: bool):
        query = self.__db.execute(self.__scripts["insert new employee"], first_name = first_name, last_name = last_name, middle_name = middle_name, phone = phone, email = email, birthdate = birthdate, avatar_url =avatar_url, company_id = company_id, is_active = is_active)
    

    # БД. Получить максимальный {id} сотрудника
    def get_max_id_employee(self, id: int):
        query = self.__db.execute(self.__scripts['get max id empl'], max_id_empl = id)
        return query.fetchall()[0][0]

    # БД. Редактирование все данные сотрудника
    def update_employee(self, employeeId: int, new_lastName: str, new_email: str, new_url: str, new_phone: int, new_isActive: bool):
        query = self.__db.execute(self.scripts['edited employee'], employeeId=employeeId, new_lastName=new_lastName, new_email=new_email, new_url=new_url, new_phone=new_phone, new_isActive=new_isActive)
        

    # БД. Удалить сотрудника по {id}
    def delete_employee_db(self, id: int):
        query = self.__db.execute(self.__scripts['delete id employee'], max_id_empl = id)
        
