from sqlalchemy import create_engine, Table, Column, Integer, String, inspect
from sqlalchemy import MetaData  #  Metadata contains definitions of tables and associated objects such as index, view, triggers, etc.
meta = MetaData()


# -------------------------------------------------
# connect to the database
# -------------------------------------------------
USER = "flaskuser"
PASSWORD = "asd"
DATABASE_NAME = "featureextractiontasks"
engine = create_engine('postgresql://'+USER+':'+PASSWORD+'@localhost:5432/'+ DATABASE_NAME, echo=True)
conn = engine.connect()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String),
   Column('lastname', String),
)

# -------------------------------------------------
# print avilable tables inside the database
# -------------------------------------------------
print(meta.tables)

# -------------------------------------------------
# Create student table
# -------------------------------------------------
'''
students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String),
   Column('lastname', String),
)

meta.create_all(engine)

# -------------------------------------------------
# Insert a raw in student table
# -------------------------------------------------

# first method
# ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')

# second method
new_raw = {"name": 'vahid', "lastname": 'ght'}
ins = students.insert().values([new_raw])

result = conn.execute(ins) # execute the command

# -------------------------------------------------
# Insert multiple raws in student table
# -------------------------------------------------
conn.execute(students.insert(), [
   {'name':'Rajiv', 'lastname' : 'Khanna'},
   {'name':'Komal','lastname' : 'Bhandari'},
   {'name':'Abdul','lastname' : 'Sattar'},
   {'name':'Priya','lastname' : 'Rajhans'},
])
'''


# -------------------------------------------------
# select all rows
# -------------------------------------------------
print(meta.tables)
s = students.select()
result = conn.execute(s)
for num, row in enumerate(result):
   print (f" {num},   {row}")
   if num == result.rowcount-1:
      break
# -------------------------------------------------
# select specific rows
# -------------------------------------------------
s = students.select().where(students.c.id>2)
result = conn.execute(s)

for num, row in enumerate(result):
   print (f" {num}:   {row}")
   if num == result.rowcount-1:
      break


s = students.select().where(students.c.name=='vahid')
result = conn.execute(s)

if result.rowcount > 0: # iterate only if there is anything from query
    for num, row in enumerate(result):
        print(f" {num}:  id: {row.id}, name: {row.name}, all {row}")
        if num == result.rowcount-1:
            break

# -------------------------------------------------
# Update row
# -------------------------------------------------
update_rule = students.update().where(students.c.id == 4).values(lastname='Kapoor')
conn.execute(update_rule)

# -------------------------------------------------
# Delete row
# -------------------------------------------------
delete_rule = students.delete().where(students.c.lastname == 'Khanna')
conn.execute(delete_rule)

