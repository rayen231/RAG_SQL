import db
con=db.create_connection("localhost", "root", "", "schoola")
print(con)
print(db.execute_query(con, "SELECT * FROM student WHERE Name = 'John';"))