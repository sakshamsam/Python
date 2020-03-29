import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("portfolioDB.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS portfolio (id INTEGER PRIMARY KEY, name TEXT, itype TEXT, amount INTEGER, sdate TEXT, ldate TEXT, anav REAL, qty REAL, holder TEXT, portal TEXT)")
        self.conn.commit()

    def insert(self, name, itype, amount, sdate, ldate, anav, qty, holder, portal):
        self.cur.execute("INSERT INTO portfolio VALUES(NULL,?,?,?,?,?,?,?,?,?)",(name, itype, amount, sdate, ldate, anav, qty, holder, portal))
        #print("inserted successfully")
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM portfolio")
        rows = self.cur.fetchall()
        return rows

    def search(self, name="", itype="", amount="", sdate="", ldate="", anav="", qty="", holder="", portal=""):
        self.cur.execute("SELECT * FROM portfolio WHERE name=? OR itype=? OR amount=? OR sdate=? OR ldate=? OR anav=? OR qty=? OR holder=? OR portal=?",(name, itype, amount, sdate, ldate, anav, qty, holder, portal))
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM portfolio WHERE id=?",(id,))
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def update(self, id, name, itype, amount, sdate, ldate, anav, qty, holder, portal):
        self.cur.execute("UPDATE portfolio SET name=?, itype=?, amount=?, sdate=?, ldate=?, anav=?, qty=?, holder=?, portal=? WHERE id=?",(name, itype, amount, sdate, ldate, anav, qty, holder, portal, id))
        #print("updated")
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def __del__(self):
        self.conn.close()


"""
connect()
#insert("DSP Multi Cap","Fund",10000,"07/02/2011","25/05/2019",35.5,21,"Sunil","Upstox")
#delete(3)
print(view())
update(id=3,name="SBI", itype="Shares", amount=9000, sdate="05/05/2017", ldate="07/10/2019", anav=60.5, qty=60.75, holder="Saksham", portal="Zerodha")
print(search(itype="Fund"))
print(view())
"""