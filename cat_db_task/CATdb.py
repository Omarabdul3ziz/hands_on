import sqlite3

conn = sqlite3.connect(r"CATdb.db")
conn.execute('''CREATE TABLE Member (
	MemberID integer PRIMARY KEY AUTOINCREMENT,
	Name text,
	LevelID integer,
	CircleID integer,
    FOREIGN KEY (LevelID) REFERENCES Level (LevelID),
    FOREIGN KEY (CircleID) REFERENCES Circle (CircleID))''')

conn.execute('''CREATE TABLE Circle (
	CircleID integer PRIMARY KEY AUTOINCREMENT,
	Name text,
	Description text,
	LeaderID integer,
	MentorID integer,
    FOREIGN KEY (LeaderID) REFERENCES Member (MemberID),
    FOREIGN KEY (MentorID) REFERENCES Member (MemberID))''')

conn.execute('''CREATE TABLE Level (
	levelID integer PRIMARY KEY AUTOINCREMENT,
	Title text,
	Description text)''')    

conn.commit()
conn.close()