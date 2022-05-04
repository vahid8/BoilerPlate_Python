#Fast subsets of large datasets with Pandas and SQLite
# There are two methods :
# 1. Chunking data
"""
We load the CSV in chunks (a series of small DataFrames),
filter each chunk by the street name, and then
concatenate the filtered rows.
Note:
    If we do this once, that’s fine. If we need to do this
    over and over again with different streets, this may not
    be acceptable performance
"""
import pandas as pd

def get_voters_on_street(name):
    return pd.concat(
       df[df["street"] == name] for df in
       pd.read_csv("voters.csv", chunksize=1000)
    )

# 2. Using SQLite as data storage for Pandas
"""
You need an index
If you want to index data that doesn’t fit in memory, 
databases support this out of the box. A database like PostgreSQL or MySQL 
can add a lot of operational overhead, though: you don’t necessarily want 
to install and maintain whole server process. And that’s where SQLite comes in.

SQLite is a fully-featured relational database that runs as library, not a server;
Python ships with built-in support. And SQLite stores its data in a single file.
Instead of having to manage one CSV file, you have to manage one SQLite database file.
"""
# 2.1. Load the data into SQLite, and create an index
import sqlite3

# Create a new database file:
db = sqlite3.connect("voters.sqlite")

# Load the CSV in chunks:
for c in pd.read_csv("voters.csv", chunksize=1000):
    # Append all rows to a new database table, which
    # we name 'voters':
    c.to_sql("voters", db, if_exists="append")
# Add an index on the 'street' column:
db.execute("CREATE INDEX street ON voters(street)")
db.close()

# 2.2 write our query function -> its 50x faster lookups than before
def get_voters_for_street(street_name):
  conn = sqlite3.connect("voters.sqlite")
  q = "SELECT * FROM voters WHERE street = ?"
  values = (street_name,)
  return pd.read_sql_query(q, conn, values)