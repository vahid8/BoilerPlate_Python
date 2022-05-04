# Content
- [python virtual env setup](#Python-virtual-env)
- [Shortcuts python](#Shortcuts-python)
- [Shortcuts pandas](#Shortcuts-pandas)
- [Shortcuts matplotlib](#Shortcuts-matplotlib)
- [Shortcuts psql terminal](#Shortcuts-psql-terminal)
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
        $ pip install virtualenv
      ```
  2. Make a new direvtory for creating files inside
      ```shell
        $ mkdir my_env
      ```
  3. Create a virtual envirnment in this dir
      ```shell
        $ py -m venv my_env
      ```
  4. Acivate the envirnment
      ```shell
        $ .\my_envScripts\activate
      ```

### Shortcuts python
| Command | Description |
| --- | --- |
| `[line.strip() for line in open(file_path,'r')]` | read the file as a list of lines
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
| `df.loc[0]` | row with index eqaul to 0 ( there should be a row with index 0 in dataframe to get result)|
| `df.iloc[0]` | Get first row without looking at index (just first row), the index can be anything  |
| `df['Date'] = pd.to_datetime(df['Date'])` | change date dtime to series to timeseries for plot |
| `df.set_index('Date', inplace=True)` | Change the first column to index column |
| `df.fillna(0, inplace=True)` | fill nan values with 0 |
| `df = df.iloc[:,0:21].apply(pd.to_numeric)` | convert values from str to numeric
| `df = df.cumsum()` | change the values of a specific column to cumulative sum |


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

### Shortcuts psql terminal
| Command | Description |
| --- | --- |
| sudo -u postgres psql | Enter postgres shel |
| \l | list of databases |
| \du | list of rules |
| \c | see which databae we are connected to now |
| \c mydatabase | connect to another database(mydatabase here) |
| \dt | see list of available tables in current database that we are connected to | 
| \d <table_name>|  see structure of the table |
| DROP TABLE IF EXISTS customers CASCADE;| Drop a table from database |
| DROP DATABASE <name>;| Drop a database |
| ALTER TABLE customers ADD COLUMN phone VARCHAR; | add a new column to the existing database |
| UPDATE customers SET contact_name = 'John Doe' WHERE id = 1; | change a value in the customers table in contact_name column and id 1 |
| ALTER TABLE customers ALTER COLUMN contact_name SET NOT NULL; | change a specific column charachteristics |

  
### Scripts description
| name | short description | 
| --- | --- | 
| Folder_to_subfolders | Split files in a folder into subfolders based on custom file numbers |
| subfolders_merger.py | merge different folders into one folder |
| argParser.py | argparse example to get the user input as argument|
| yaml_reader.py | yaml example to read the yaml file and a sample yaml file |
| merge_pdf_images.py | read pdf and images, convert them to each other and concat or split them |
 
