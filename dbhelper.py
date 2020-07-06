import sqlite3


class DBHelper:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)
        self.setup()

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS persona ( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, nombre VARCHAR (255) NOT NULL UNIQUE);"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, item_text):
        stmt = "INSERT INTO persona (nombre) VALUES (?)"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text):
        stmt = "DELETE FROM persona WHERE persona.nombre = (?)"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self):
        print('select')
        stmt = "SELECT nombre FROM persona"
        return [x[0] for x in self.conn.execute(stmt)]