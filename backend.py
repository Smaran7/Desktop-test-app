import sqlite3

def connect():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Book (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
    con.commit()
    con.close()

def insert(Title,Author,Year,ISBN):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("INSERT INTO Book VALUES (NULL,?,?,?,?)",(Title,Author,Year,ISBN))
    con.commit()
    con.close()

def view():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Book")
    rows=cur.fetchall()
    con.close()
    return rows

def search(Title="",Author="",Year="",ISBN=""):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Book WHERE Title=? OR Author=? OR Year=? OR ISBN=?",(Title,Author,Year,ISBN))
    rows=cur.fetchall()
    con.close()
    return rows

def delete(id):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("DELETE FROM Book WHERE id=?",(id,))
    con.commit()
    con.close()

def update(id,Title,Author,Year,ISBN):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("UPDATE Book SET Title=? , Author=? , Year=? , ISBN=? WHERE id=?",(Title,Author,Year,ISBN,id))
    con.commit()
    con.close()
