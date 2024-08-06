from sqlalchemy import create_engine
from sqlalchemy.sql import text

class CompanyTable:
    __scripts = {
        "select": text("select * from company"),
        "select by id": text("select * from company where id = :company_id"),
        "select isActive": text("select * from company where \"is_active\" = true"),
        "delete by id": text("delete from company  where id = :id_to_delete"),
        "insert company": text("insert into company (\"name\", \"description\") values (:new_name, :new_descr)"),
        "get max id": text("select MAX(id) from company"),
        "select empl list": text("select * from employee where company_id = :id"),
    }
    

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    # БД. Запросить список организации
    def get_company_list(self):
        query = self.__db.execute(self.__scripts["select"])
        return query.fetchall()

    # БД. Запросить организацию по {id}
    def get_company_by_id(self,id: int):
        query =  self.__db.execute(self.__scripts["select by id"], company_id = id)
        return query.fetchall()

    # БД. Запросить список  активных организаций
    def get_active_company(self):
        query = self.__db.execute(self.__scripts["select isActive"])
        return query.fetchall()

    #БД. Удалить организацию {id}
    def delete_company(self, id: int):
        query = self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)
        return query.fetchall()

    # БД. Создать организацию с названием {name}:{description}
    def create_comp(self, name: str, description: str):
        query = self.__db.execute(self.__scripts["insert company"], new_name = name, new_descr = description)
        return query.fetchall()

    # БД. Получить максимальный {id} организации")
    def get_max_id_comp(self, id: int):
        query = self.__db.execute(self.__scripts["get max id"], max_id = id)
        return query.fetchall()[0][0]

    # БД. Получить список сотрудников организации {company_id}"
    def get_empl_list_db(self, company_id: int):
        query = self.__db.execute(self.__scripts["select empl list"], id = company_id)
        return query.fetchall()