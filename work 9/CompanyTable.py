import allure
from sqlalchemy import create_engine
from sqlalchemy.sql import text


class CompanyTable:
    __scripts = {
        "select": 'select * from company where deleted_at is null',
        "select_only_active": 'select * from company '
                              'where deleted_at is null '
                              'and is_active = true',
        "delete_by_id": text("DELETE FROM company WHERE id = :id_to_delete"),
        "insert new": text("INSERT INTO company(\"name\", description) "
                           "VALUES (:new_name, :new_description)"),
        "get_max_id": text("SELECT MAX(id) FROM company"),
        "select_by_id": text('SELECT * FROM company '
                             'WHERE id = :select_id '
                             'AND deleted_at is null')
    }

    def __init__(self, db_connection_string: str) -> None:
        self.db = create_engine(db_connection_string)

    @allure.step('Delete company from DB by id')
    def delete(self, id: int) -> None:
        '''
        Delete company by id
        '''
        self.db.execute(self.__scripts["delete_by_id"], id_to_delete=id)

    @allure.step('Create company in DB')
    def create(self, name: str, description: str) -> None:
        '''
        Create company
        '''
        self.db.execute(self.__scripts["insert new"], new_name=name,
                        new_description=description)

    @allure.step('Get max company id from DB')
    def get_max_id(self) -> int:
        '''
        Get max company id (last created company)
        '''
        return self.db.execute(self.__scripts["get_max_id"]).fetchall()[0][0]