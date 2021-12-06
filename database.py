import sqlite3

class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.c=self.con.cursor()
        self.c.execute("""
                        CREATE TABLE IF NOT EXISTS datas(
                        pid INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        price TEXT NOT NULL,
                        status TEXT NOT NULL,
                        serial TEXT NOT NULL,
                        stock TEXT NOT NULL,
                        exp TEXT NOT NULL
                        )
                        """)
        self.con.commit()

    def insert(self,name,price,status,serial,stock,exp):
        sql="""
            insert into datas values(NULL,?,?,?,?,?,?)
        """
        self.c.execute(sql,(name,price,status,serial,stock,exp))
        self.con.commit()

    def fetch_record(self):
        self.c.execute("SELECT * FROM datas")
        data = self.c.fetchall()
        return data
    

    def update_record(self,name,price,status,serial,stock,exp,pid):
        sql="""
            update datas set name=?,price=?,status=?,serial=?,stock=?,exp=? where pid=?
        """
        self.c.execute(sql,(name,price,status,serial,stock,exp,pid))
        self.con.commit()

    def remove_record(self,pid):
        sql="delete from datas where pid=?"
        self.c.execute(sql,(pid,))
        self.con.commit()


