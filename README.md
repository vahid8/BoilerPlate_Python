# Boilerplate_Python

## Shortcuts python
| Command | Description |
| --- | --- |
| `[item[0] for item in os.walk(path)` | get all dirs (inclouding route) and all child folders |
| `a = np.empty((0,3), int)` | Create a new numpy for appending or stacking |
| `img = np.zeros([100,100,3],dtype=np.uint8) then img.fill(255) # or img[:] = 255` | create an empty black or white image
| `min = a if a < b else b` | Ternary operation


## Shortcuts numpy
| Command | Description |
| --- | --- |
| `a = np.empty((0,3), int)` | Create a new numpy for appending or stacking |
| `id_x = np.where((points[:,0] > x_min) & (points[:,0] < x_max))` | Get the id of desired part by filtering|
| `id_x =  points[:,0] > x_min) & (points[:,0] < x_max` | Get boolean array to filter data|
| `np.linspace(min_value, max_value, num=int((max-min)/dist),endpoint=True)` | Create data or points between two number|
| `np.min(points,axis =0),np.max(points,axis =0),np.mean(points,axis =0)` | Get Min, Max, Mean of points
| `points3D = np.vstack((f.x, f.y, f.z)).transpose()` | From las files to numpy in n*3 format

# Scripts description
All handy scripts. Deciption of functions:
- [Folder To Subfolders](#Folder_to_subfolders)
- [read change json labels](#Read Change Json lables)


| name | short description | 
| --- | --- | 
| Folder_to_subfolders | split files in a folder into subfolders |
| read change json labels | read segmentation labels in json format and change desired label and also check typos |


#### Folder_to_subfolders
Get the input dir and copy all files inside into output_dir and in different subfolders based on number of files you give as input
```More description:
You have a folder with large number of files that you want to split into some folders with fewer number of files in each
```
