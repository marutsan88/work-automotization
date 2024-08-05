from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"

# получить список таблиц
def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[1] == 'company'

def test_select_params():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from employee where \"last_name\" = :last_name and \"company_id\" >= :company_id")
    params = {
        'last_name': 'Семирунний',
        'company_id': 2986
    }
    rows = db.execute(sql_statement, params).fetchall()

    assert len(rows) == 0

def test_insert_company():
    db = create_engine(db_connection_string)
    sql = text("insert into company (\"name\") values (:new_name)")
    rows = db.execute(sql, new_name = 'SkyPro')


def test_update_company():
    db = create_engine(db_connection_string)
    sql = text("update company set description = :descr where id = :company_id")
    rows = db.execute(sql, descr = 'Шиномотажка', company_id = 2810)

def test_update_employee():
    db = create_engine(db_connection_string)
    sql = text("update employee set last_name = :last_name, phone = :phone, email = :mail, avatar_url = :url, is_active = :is_active  where id = :employee_id")
    rows = db.execute(sql, last_name = 'Sidorov', phone = '89176258545', mail = 'sidorov@mail.ru', url = 'opa', is_active = False, employee_id = 1934)

def test_delete_emloyee():
    db = create_engine(db_connection_string)
    sql = text("delete from employee where id = :employee_id")
    rows = db.execute(sql, employee_id = 1933)

def test_delete_company():
    db = create_engine(db_connection_string)
    sql = text("delete from company  where id = :id")
    rows = db.execute(sql, id = 2445)