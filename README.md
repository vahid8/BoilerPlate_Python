# Content
- [python virtual env setup](#Python-virtual-env)
- [Shortcuts python](#Shortcuts-python)
- [Shortcuts pandas](#Shortcuts-pandas)
- [Shortcuts matplotlib](#Shortcuts-matplotlib)
- [Shortcuts pathlib](#Shortcuts-pathlib)
- [Shortcuts laspy](#Shortcuts-laspy)
- [shortcuts pcl](#shortcuts-pcl)
- [Shortcuts psql terminal](#Shortcuts-psql-terminal)
- [Shortcuts mongodb](#Shortcuts-mongodb)
- [Scripts description](#Scripts-description)

### Python Virtual Env
#### Ubuntu Setup
use the following procedure to setup a new virtual env
  1. Install venv package using pip
      ```shell
        $ sudo apt install python3-venv
      ```
  2. Make a new direvtory for creating files inside
      ```shell
        $ mkdir my_env
      ```
  3. Create a virtual envirnment in this dir
      ```shell
        $ python3 -m venv my_env
      ```
  4. Acivate the envirnment
      ```shell
        $ source my_env/bin/activate
      ```
  * To install packages listed in requirments.txt
      ```shell
        $ pip install -r requirments
      ``` 
  * To deactivate the virtual environment
      ```shell
        $ deactivate
      ```
  * To get list of packages installed inside a virtual envirnment
      ```shell
        pip freeze
      ```
  * To save them in a txt
      ```shell
        pip freeze > requirments.txt
      ```
#### windows setup on cmd
  1. Install venv package using pip
      ```shell
        pip install virtualenv
      ```
  2. Make a new direvtory for creating files inside
      ```shell
        mkdir my_env
      ```
  3. Create a virtual envirnment in this dir
      ```shell
        python -m venv my_env
      ```
  4. Acivate the envirnment
      ```shell
        .\my_env\Scripts\activate
      ```

### Shortcuts python
| Command | Description |
| --- | --- |
| `[line.strip() for line in open(file_path,'r')]` | read the file as a list of lines |
| `[f.write(line + "\n") for line in lines]` |  Write a list of (string)lines in to a file  |
| `[item[0] for item in os.walk(path)` | get all dirs (inclouding route) and all child folders |
| `os.path.splitext("file.gzip.txt")[0])` | Get the filename without suffix (result here: file.gzip)
| `pathlib.Path("file.gzip.txt").stem` | Get the filename without suffix (result here: file.gzip)
| `pathlib.Path("media/file.txt").name` | Get the filename without path (result here: file.txt)
| `os.path.split("path")` | split the path in head and tail
| `min = a if a < b else b` | Ternary operation
| `squares = list(map(lambda x: x ** 2, numbers))`| map
| `evens = list(filter(lambda x: x % 2 == 0, numbers))` | filter
| `product = reduce(lambda x, y: x * y, numbers)` | reduce
```example
path                             head                 tail
'/home/user/Desktop/file.txt'   '/home/user/Desktop/'   'file.txt'
'/home/user/Desktop/'           '/home/user/Desktop/'    {empty}
'file.txt'                           {empty}            'file.txt'
```

nametuple
```
import collections
Car = collections.namedtuple('Car', ['color','mileage'])
my_car = Car('red', 3812.4)
print(my_car.color)
```

### Shortcuts pandas
| Command | Description |
| --- | --- |
| `grouped = gdf.groupby("poly_num") then for name, group in grouped:` | Group and iterate |
| `df.drop(['B', 'C'], axis=1, inplace=True)` | drop columns B, C |
| `df.drop([0, 5 ,6])` | drop rows 0, 5, 6 |
| `group = pd.concat([group, new_df], ignore_index=True)` | append new df to existing df |
| `dataframe['geometry'] = dataframe.apply(lambda row: Point(row.X, row.Y, row.Z), axis=1)` | Cretae new column based on other columns |
| `asbruch_df = dataframe[dataframe["class"] == "ausbruch"]` | filter based on a column value |
| `df = df.filter(items = [index to keep], axis=0)` | Filter Pandas rows DataFrame Based on Index |
| `new_df = df[["image_name", "x", "y", "z", "H", "R", "P"]] | Filter pandas based on column names -> keep only what is necessary |
| `df.loc[0]` | row with index eqaul to 0 ( there should be a row with index 0 in dataframe to get result)|
| `df.iloc[0]` | Get first row without looking at index (just first row), the index can be anything  |
| `df['Date'] = pd.to_datetime(df['Date'])` | change date dtime to series to timeseries for plot |
| `df.set_index('Date', inplace=True)` | Change the first column to index column |
| `df.fillna(0, inplace=True)` | fill nan values with 0 |
| `df = df.iloc[:,0:21].apply(pd.to_numeric)` | convert values from str to numeric
| `df = df.cumsum()` | change the values of a specific column to cumulative sum |
| `df = df.round({'X': 4, "Y": 4, "Z": 4})` | round column X, Y, Z to 4 Deci digits |


### Shortcuts matplotlib
plotting 4 images in a plt
```
for idx in range(4):
    ax = plt.subplot(2, 2, idx + 1)
    ax.imshow(images[idx])
    ax.set_title(f"prediction: {class_dict[predictions[idx]]}\n target: {class_dict[targets[idx]]}")

plt.tight_layout()
plt.show()
```
plot 2d histogram of heights or intensity
```
    fig = plt.figure()
    ax = fig.add_subplot()
    surf = ax.scatter(x_points, y_points,s=0.1, c=z_points, cmap=cm.jet)
    cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
    cbar.ax.set_xlabel('Height[m]')
    ax.set_title(f"H_min[m]: {min_h}")
    ax.plot(polygon3d[0], polygon3d[1], color="black", linewidth=2)
    plt.savefig(os.path.join(out_dir, str(_id) + '_height.jpg'))
    plt.close()

```

### Shortcuts pathlib
``` from pathlib import Path ```
| Command | Description |
| --- | --- |
| `[item for item in input_dir.iterdir() if item.name.endswith(".las")]` | get files |
| `if Path.PurePosixPath(cam_pos_path).suffixes[0] == ".shp"` | check suffix |
| `if Path("/path/to/file").is_file():` | check if the file exists |
| `if Path("/path/to/file").is_dir():` | check if the dir exists |
| `if Path("/path/to/file").exists():` | check if the path exist (file or dir) |




### Shortcuts laspy
##### Open and read the file
```
with laspy.open("Test_LAS.las", mode='r') as open_file:
    las = open_file.read()
```
##### Read xyz as an np array with shape (n,3)
```
points =las.xyz
```

##### see all available point properties 
```
 point_format = las.point_format
 print(list(point_format.dimension_names))
 # result : ['X', 'Y', 'Z', 'intensity', 'return_number', 'number_of_returns' ,... ]
```
##### filter and save base on classification
```
with laspy.open("Vahid_Test_LAS.las", mode='r') as open_file:
    las = open_file.read()
    new_file = laspy.create(point_format=las.header.point_format, file_version=las.header.version)
    new_file.points = las.points[las.classification == 5]   
    new_file.write("class_5.las")
```
### Shortcuts pcl
##### install ubuntu 20.04
sudo apt-get install python3-pcl pcl-tools
##### convert numpy to pcl object
points = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]], dtype=np.float32)
cloud = pcl.PointCloud(points)
for point in cloud:
    print("(%f, %f, %f)" % (point[0], point[1], point[2]))

### Shortcuts psql terminal
| Command | Description |
| --- | --- |
| sudo apt install postgis postgresql-12-postgis-3 | install postGIS for postgres-12 |
| systemctl status postgresql or stop postgresql or start postgresql | to see the status, start or stop |
| sudo -u postgres psql | Enter postgres shel | ---- |
| CREATE USER vahid WITH ENCRYPTED PASSWORD '123456'; | Create a new role |
| ALTER USER vahid WITH SUPERUSER;| --- |
| ALTER USER vahid WITH CREATEDB | --- |
| \l | list of databases |
| CREATE DATABASE myName OWNER vahid |  create a database called myName with the vahid ownership |
| GRANT ALL PRIVILEGES ON DATABASE myName to vahid;| --- |
| \du | list of rules |
| \c | see which databae we are connected to now |
| \c mydatabase | connect to another database(mydatabase here) |
| CREATE EXTENSION postgis;| activate postGIS on the current database
| \dt | see list of available tables in current database that we are connected to | 
| \d <table_name>|  see structure of the table |
| DELETE FROM "myTable"; | delete all records of a table |
| DROP TABLE IF EXISTS customers CASCADE;| Drop a table from database |
| ALTER DATABASE name RENAME TO new_name; | Renmae the DB |
| DROP DATABASE <name>;| Drop a database |
| ALTER TABLE customers ADD COLUMN phone VARCHAR; | add a new column to the existing database |
| UPDATE customers SET contact_name = 'John Doe' WHERE id = 1; | change a value in the customers table in contact_name column and id 1 |
| ALTER TABLE customers ALTER COLUMN contact_name SET NOT NULL; | change a specific column charachteristics |

  
### Shortcuts mongodb
| Command | Description |
| --- | --- |
| sudo systemctl start mongod | start mongo db |
| sudo systemctl status mongod | verify it has started |
| sudo systemctl stop mongod  | stop it |
| mongosh | begin using it |
  
 commands insisde the mongo sh   
  
| Command | Description |
| --- | --- |
| db.version() | check the version of mongo |
| db.stats() | check avilable databses |
| sudo systemctl status mongod | verify it has started |
| sudo systemctl stop mongod  | stop it |
| mongosh | begin using it |
| use DataBASE_NAME | create a new database if not exist | 
| db | check the current selelcted db |
| db.movie.insertOne({"name": "vahid"}) | insert a document (record) to the database (here the movie collection) |
| show dbs | show avilable dbs with at least one record in it |
| db.dropDatabase() | delete the selected database |
| db.createCollection(name, options) | cretae collection |
| db.createCollection(name, {autoIndexId: true}) | cretae collection with auto index |
| show collections | show collections on current db |
| db.COLLECTION_NAME.drop() |  drop a collection from current db | 
| db.COLLECTION_NAME.find() | get all documents(records) inside a  collection |
| db.COLLECTION_NAME.find().pretty() | show the result in a readbale format |
| db.COLLECTION_NAME.findOne({"name": "vahid"}) | get only first documents(records) with the name vahid |
| db.COLLECTION_NAME.find({"likes": {$lt:50}}).pretty() | filter documents with number of likes lt(less than 50) |
| db.COLLECTION_NAME.find({"likes": {$lte:50}}).pretty() | filter documents with number of likes lte(less than and equal to 50) |
| db.COLLECTION_NAME.find({"likes": {$gte:50}}).pretty() | filter documents with number of likes gte(greater than and equal to 50) |
| db.COLLECTION_NAME.find({"likes": {$ne:50}}).pretty() | filter documents with number of likes ne(not equal to 50) |
| db.COLLECTION_NAME.find({$and:[ {"likes": {$ne:50}}, {"name": "vahid"} ] }).pretty() | filter documents with number of likes ne(not equal to 50) and the name eqaul to vahid|
| db.COLLECTION_NAME.find({$or:[ {"likes": {$ne:50}}, {"name": "vahid"} ] }).pretty() | filter documents with number of likes ne(not equal to 50) or the name eqaul to vahid|
| db.COLLECTION_NAME.find({},{KEY_1:1, KEY_2:0}) | show the result and only fields that are 1 (projection concept) |
| db.COLLECTION_NAME.find({},{_id:0, 'title':1}) | show the title for all documents |
| db.COLLECTION_NAME.find({},{_id:0, 'title':1}).limit(NUMBER) | show the title for only limited documents documents |
| db.COLLECTION_NAME.find({}).sort({KEY:1}) | sort the result based on the key 1 means ascending and -1 means descending |
| db.COLLECTION_NAME.update_one(SELECTION_CRITERIA, UPDATE_DATA) | update the data |
| db.COLLECTION_NAME.update_one({'title': 'mySample'}, {$set:{'title': 'newTitle'}}) | update the data on first founded document |
| db.COLLECTION_NAME.update_one({'title': 'mySample'}, {$set:{'title': 'newTitle'}} {multi: true}) | update the data on all founded documents |
| db.COLLECTION_NAME.remove(DELETION_CRITERIA) | remove all documents with the criteria |
| db.COLLECTION_NAME.remove({'title': 'mySample'}) | remove all documents with the title mySample |
| db.COLLECTION_NAME.remove({DELETION_CRITERIA} {justOne:true}) | remove only one documents with the criteria |
  
### Scripts description
| name | short description | 
| --- | --- | 
| Folder_to_subfolders | Split files in a folder into subfolders based on custom file numbers |
| subfolders_merger.py | merge different folders into one folder |
| argParser.py | argparse example to get the user input as argument|
| yaml_reader.py | yaml example to read the yaml file and a sample yaml file |
| merge_pdf_images.py | read pdf and images, convert them to each other and concat or split them |
 
