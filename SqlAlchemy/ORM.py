from sqlalchemy import create_engine, Table, Column, Integer, String, inspect
from sqlalchemy import MetaData  #  Metadata contains definitions of tables and associated objects such as index, view, triggers, etc.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

meta = MetaData()


# -------------------------------------------------
# Database config
# -------------------------------------------------
USER = "flaskuser"
PASSWORD = "asd"
DATABASE_NAME = "featureextractiontasks"
engine = create_engine('postgresql://'+USER+':'+PASSWORD+'@localhost:5432/'+ DATABASE_NAME, echo=True)


'''
The main objective of the Object Relational Mapper API of SQLAlchemy is to facilitate associating user-defined Python 
classes with database tables, and objects of those classes with rows in their corresponding tables.
'''
# -------------------------------------------------
# Create a class for the new table and create table in database
# -------------------------------------------------
Base = declarative_base()

class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key=True)

   name = Column(String)
   address = Column(String)
   email = Column(String)

Base.metadata.create_all(engine)


'''
In order to interact with the database, we need to obtain its handle. A session object is the handle to database. 
Session class is defined using sessionmaker()
'''
# -------------------------------------------------
# Connect to the database
# -------------------------------------------------
Session = sessionmaker(bind=engine)
session = Session()

# -------------------------------------------------
# Add a new row
# -------------------------------------------------
c1 = Customers(name = 'Ravi Kumar', address='Station Road Nanded', email='ravi@gmail.com')

session.add(c1)
session.commit()


# -------------------------------------------------
# Add multiple row
# -------------------------------------------------
session.add_all([
   Customers(name = 'Komal Pande', address = 'Koti, Hyderabad', email = 'komal@gmail.com'),
   Customers(name = 'Rajender Nath', address = 'Sector 40, Gurgaon', email = 'nath@gmail.com'),
   Customers(name = 'S.M.Krishna', address = 'Budhwar Peth, Pune', email = 'smk@gmail.com')]
)

session.commit()

# -------------------------------------------------
# make query for all available data in a table
# -------------------------------------------------
result = session.query(Customers).all()
for row in result:
   print ("id: ",row.id,"Name: ",row.name, "Address:",row.address, "Email:",row.email)
#    db.session.selete(row) if you want to delete the row
#    db.session.commit()


# -------------------------------------------------
# make query for a specific data in the table
# -------------------------------------------------
result = session.query(Customers).filter(Customers.id != 3).all()
for row in result:
   print ("id: ",row.id,"Name: ",row.name, "Address:",row.address, "Email:",row.email)

# -------------------------------------------------
# make query for a specific data in the table and keep only the first
# -------------------------------------------------
x = session.query(Customers).filter(Customers.id != 3).first()
print ("id: ",x.id,"Name: ",x.name, "Address:",x.address, "Email:",x.email)

# -------------------------------------------------
# update a row -> first query then make change and commit
# -------------------------------------------------
print("before updating")
x = session.query(Customers).get(2)  # just another way to query by id
print ("id: ",x.id,"Name: ",x.name, "Address:",x.address, "Email:",x.email)

x.address = 'Bozorgmehr str'
session.commit()

print("after updating")
x = session.query(Customers).get(2)  # just another way to query by id
print ("id: ",x.id,"Name: ",x.name, "Address:",x.address, "Email:",x.email)

'''
For bulk updates, we shall use update() method of the Query object. 
Let us try and give a prefix, ‘Mr.’ to name in each row (except ID = 2).
The corresponding update() statement is as follow
'''
session.query(Customers).filter(Customers.id != 2).update({Customers.name:"Mr."+Customers.name},
                                                          synchronize_session = False)

'''
There other keyword for filtering see a full list here:
https://flask-sqlalchemy.palletsprojects.com
'''

'''
USe table relations with the ForeignKey('customers.id')
more info 
https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_building_relationship.htm
'''
