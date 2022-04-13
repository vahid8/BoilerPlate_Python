# Content
- [python virtual env setup](#Python-virtual-env)
- [Shortcuts python](#Shortcuts-python)
- [Shortcuts pandas](#Shortcuts-pandas)
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
| `min = a if a < b else b` | Ternary operation
| `os.path.splitext("file.gzip.txt")[0])` | Get the filename without suffix (result here: file.gzip)
| `os.path.split("path")` | split the path in head and tail
```example
path                             head                 tail
'/home/user/Desktop/file.txt'   '/home/user/Desktop/'   'file.txt'
'/home/user/Desktop/'           '/home/user/Desktop/'    {empty}
'file.txt'                           {empty}            'file.txt'
```

### Shortcuts pandas
| Command | Description |
| --- | --- |
| `grouped = gdf.groupby("poly_num") then for name, group in grouped:` | Group and iterate |
| `df.drop(['B', 'C'], axis=1)` | drop columns B, C |
| `df.drop([0, 5 ,6])` | drop rows 0, 5, 6 |
| `group = pd.concat([group, new_df], ignore_index=True)` | append new df to existing df |
| `dataframe['geometry'] = dataframe.apply(lambda row: Point(row.X, row.Y, row.Z), axis=1)` | Cretae new column based on other columns |
| `asbruch_df = dataframe[dataframe["class"] == "ausbruch"]` | filter based on a column value |


### Scripts description
| name | short description | 
| --- | --- | 
| Folder_to_subfolders | Split files in a folder into subfolders based on custom file numbers |
| subfolders_merger.py | merge different folders into one folder |
| argParser.py | argparse example to get the user input as argument|
| yaml_reader.py | yaml example to read the yaml file and a sample yaml file |
| merge_pdf_images.py | read pdf and images, convert them to each other and concat or split them |
 
