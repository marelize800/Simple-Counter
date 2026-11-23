import sqlite3 as sq

def create_db():
	db = 'assets.db'
	with sq.connect(db) as con:
		cur = con.cursor()
		cur.execute('''
			CREATE TABLE IF NOT EXISTS users(
				id integer primary key,
				name text,
				qty integer
				)
			''')
		con.commit()

def add_user(name,qty):
	db = 'assets.db'
	with sq.connect(db) as con:
		cur = con.cursor()
		cur.execute('INSERT INTO users (name,qty) VALUES (?,?)',(name,qty))
		con.commit()

def display_data():
	db = 'assets.db'
	with sq.connect(db) as con:
		cur = con.cursor()
		cur.execute('SELECT * FROM users')

		return cur.fetchall()
			

def update(name,qty):
	db = 'assets.db'
	with sq.connect(db) as con:
		cur = con.cursor()
		cur.execute('UPDATE users SET qty=? WHERE name=?',(qty,name))
		con.commit()