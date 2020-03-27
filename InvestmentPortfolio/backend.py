import sqlite3

def connect():
    conn = sqlite3.connect("portfolioDB.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS portfolio (id INTEGER PRIMARY KEY, name TEXT, itype TEXT, amount INTEGER, sdate TEXT, ldate TEXT, anav REAL, qty REAL, holder TEXT, portal TEXT)")
    conn.commit()
    conn.close()

def insert(name, itype, amount, sdate, ldate, anav, qty, holder, portal):
    conn = sqlite3.connect("portfolioDB.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO portfolio VALUES(NULL,?,?,?,?,?,?,?,?,?)",(name, itype, amount, sdate, ldate, anav, qty, holder, portal))
    print("inserted successfully")
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("portfolioDB.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM portfolio")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(name="", itype="", amount="", sdate="", ldate="", anav="", qty="", holder="", portal=""):
    conn = sqlite3.connect("portfolioDB.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM portfolio WHERE name=? OR itype=? OR amount=? OR sdate=? OR ldate=? OR anav=? OR qty=? OR holder=? OR portal=?",(name, itype, amount, sdate, ldate, anav, qty, holder, portal))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("portfolioDB.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM portfolio WHERE id=?",(id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def update(id, name, itype, amount, sdate, ldate, anav, qty, holder, portal):
    conn = sqlite3.connect("portfolioDB.db")
    cur = conn.cursor()
    cur.execute("UPDATE portfolio SET name=?, itype=?, amount=?, sdate=?, ldate=?, anav=?, qty=?, holder=?, portal=? WHERE id=?",(name, itype, amount, sdate, ldate, anav, qty, holder, portal, id))
    print("updated")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()

"""
#insert("DSP Multi Cap","Fund",10000,"07/02/2011","25/05/2019",35.5,21,"Sunil","Upstox")
#delete(3)
print(view())
update(id=3,name="SBI", itype="Shares", amount=9000, sdate="05/05/2017", ldate="07/10/2019", anav=60.5, qty=60.75, holder="Saksham", portal="Zerodha")
print(search(itype="Fund"))
print(view())
"""