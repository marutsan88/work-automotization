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

    def __init__(self, db_connection_string):
        self.db = create_engine(db_connection_string)

    def delete(self, id):
        self.db.execute(self.__scripts["delete_by_id"], id_to_delete=id)

    def create(self, name, description):
        self.db.execute(self.__scripts["insert new"], new_name=name,
                        new_description=description)

    def get_max_id(self):
        return self.db.execute(self.__scripts["get_max_id"]).fetchall()[0][0]