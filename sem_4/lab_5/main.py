from sqlite3 import OperationalError
import sqlite3


def connect_to_db(path_to_db: str) -> sqlite3.Connection:
    print('Подключение к БД')
    try:
        conn = sqlite3.connect(path_to_db)
    except sqlite3.DatabaseError:
        print(f'Не удалось подключиться к БД: {path_to_db}')
    return conn


def create_table(conn):
    try:
        cursor = conn.cursor()
        sql = "CREATE TABLE user (id int, height real, name text, deleted bool, created DATETIME)"
        cursor.execute(sql)
    except OperationalError as e:
        print(e)


def read(conn):
    try:
        cursor = conn.cursor()
        crud_read_str = "SELECT * FROM user;"
        crud_res = cursor.execute(crud_read_str)
        print(cursor.fetchall())
        for r in crud_res:
            print(r)
    except OperationalError as e:
        print('Такой таблицы нет:', e)
        try:
            create_sql = "CREATE TABLE user (id int, height real, name text, deleted bool)"
            conn.execute(create_sql)
        except:
            print('Таблица не создана, ошибка')


def insert_values(conn, data_tuple):
    try:
        cursor = conn.cursor()
        insert_sql = "INSERT INTO user VALUES (:id, :height, :name, :deleted, :created)"
        cursor.execute(insert_sql, data_tuple)
        conn.commit()

    except sqlite3.Error as error:
        print('Ошибка при добавление данных: ', error)


def delete(conn):
    try:
        cursor = conn.cursor()
        crud_del_str = "DELETE FROM user WHERE name == 'paul'"
        crud_res = cursor.execute(crud_del_str)

        print('-' * 40)
        crud_read_str = "SELECT * FROM user"
        crud_res = conn.execute(crud_read_str)

        for r in crud_res:
            print(r)
    except conn.Error as error:
        print(error)


def update(conn):
    try:
        cursor = conn.cursor()
        crud_update_str = "UPDATE user SET deleted = 1 WHERE id == 1"
        cursor.execute(crud_update_str)
        conn.commit()
    except conn.Error as error:
        print(error)


DB_name = 'zhukov1.db'
c = connect_to_db(DB_name)
create_table(c)
insert_values(c)
read(c)
update(c)
delete(c)


