# Boilerplate_Python

## Shortcuts
| Command | Description |
| --- | --- |
| `[item[0] for item in os.walk(path)` | get all dirs (inclouding route) and all child folders |
| `a = np.empty((0,3), int)` | Create a new numpy for appending or stacking |
| `img = np.zeros([100,100,3],dtype=np.uint8) then img.fill(255) # or img[:] = 255` | create an empty black or white image
| `min = a if a < b else b` | Ternary operation

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
