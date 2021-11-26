# Boilerplate_Python

## Shortcuts python
| Command | Description |
| --- | --- |
| `[item[0] for item in os.walk(path)` | get all dirs (inclouding route) and all child folders |
| `min = a if a < b else b` | Ternary operation

## Shortcuts pytorch
| Command | Description |
| --- | --- |
| `keypoints = outputs["instances"].pred_keypoints.to("cpu").detach().numpy()` | pytorch tensor to numpy |

## Shortcuts opencv
| Command | Description |
| --- | --- |
| `img = cv2.circle(img, center, radius=5, color=(0,0, 255), thickness=2)` | draw circle |
| `img = cv2.rectangle(img, rect_start, rect_end, color=(0,0, 255), thickness=2)` | draw rectangle |


## Shortcuts numpy
| Command | Description |
| --- | --- |
| `a = np.empty((0,3), int)` | Create a new numpy for appending or stacking |
| `img = np.zeros([100,100,3],dtype=np.uint8) then img.fill(255) # or img[:] = 255` | create an empty black or white image
| `id_x = np.where((points[:,0] > x_min) & (points[:,0] < x_max))` | Get the id of desired part by filtering|
| `id_x =  points[:,0] > x_min) & (points[:,0] < x_max` | Get boolean array to filter data|
| `np.linspace(min_value, max_value, num=int((max-min)/dist),endpoint=True)` | Create data or points between two number|
| `np.min(points,axis =0),np.max(points,axis =0),np.mean(points,axis =0)` | Get Min, Max, Mean of points
| `points3D = np.vstack((f.x, f.y, f.z)).transpose()` | From las files to numpy in n*3 format
| `np.linalg.norm(ppts2d - np.array([x, y]), axis=1)` | Calc distance of a vec elements to a point
| `diff_to_min = ppts2d - np.array([x, y])` | Calc difference of a vec elements to a point (signed)
| `filter_axe = np.all(diff_to_min > 0, axis=1)` | find 2d points bigger than desired values in both x, y


## Shortcuts Searching
#### KDTree
```
from sklearn.neighbors import KDTree
centers = np.array(centers)
centers_tree = KDTree(centers) # create tree of centers
nearest_dist, nearest_idx = centers_tree.query(cam_6degree["pos"][:2].reshape(1,2), k=4) # search for 4 NEAREST CENTERS to the cam pos
```
## Shortcuts GIS
#### cluster points that are colser than a threshold distance together 
``` 
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=epsilon, min_samples=min_samples).fit(X)
labels = db.labels_
classified_points = {}
for i in range(len(np.unique(labels))):  
    mask = np.where(labels == i)  
    classified_points[i] = X[mask]  
```

#### Write features to shapefiles
``` 
option1:
left_edge_points = list(map(Point, all_points_3d_left_edge))
gdf = geopandas.GeoDataFrame(geometry=left_edge_points)
    if len(gdf) > 0:
        gdf.to_file(os.path.join(output_folder, "shapefiles", "left_edge_points.shp"))
option2:
    with fiona.open(os.path.join(output_folder, "shapefiles", "left_edge_line.shp")
            , 'w', 'ESRI Shapefile', {"geometry": "MultiLineString"}) as c:
        ## If there are multiple geometries, put the "for" loop here
        c.write({
            'geometry': mapping(complete_edges),
        })

```


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
