# Boilerplate_Python

## Shortcuts python
| Command | Description |
| --- | --- |
| `[item[0] for item in os.walk(path)` | get all dirs (inclouding route) and all child folders |
| `min = a if a < b else b` | Ternary operation
| `os.path.splitext("file.gzip.txt")[0])` | Get the filename without suffix (result here: file.gzip)

## Shortcuts pytorch
| Command | Description |
| --- | --- |
| `keypoints = outputs["instances"].pred_keypoints.to("cpu").detach().numpy()` | pytorch tensor to numpy |

## Shortcuts opencv
| Command | Description |
| --- | --- |
| `img = cv2.resize(img, (800, 600))` | resize image
| `gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` | gray image from BGR |
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
#### Reading and getting info about geodatabase using arcpy 
``` 
arcpy.env.workspace  =r"D:\EssenApp\output\ZEB1\ZEB_2019_2020_2\Bewertungsabschnitte_neu4_TUEV_1990.gdb"
# print(f"print(arcpy.ListFeatureCLasses(aa)){arcpy.ListFeatureCLasses(aa)}")
aa = arcpy.ListTables("*")
bb = arcpy.ListFeatureClasses()
print(f"arcpy.ListTables(){aa}")
print(f"arcpy.ListFeatureClasses(){bb}")
for feature in bb:
    print(feature)
    for f in arcpy.ListFields(feature):
        print(f.name)  
```


#### Write features to shapefiles
``` 
from shapely.geometry import Polygon,Point
import geopandas
all_points_3d_left_edge = [[x1,y1,z1], ... , [xn,yn,zn]]
option1:
left_edge_points = list(map(Point, all_points_3d_left_edge))
gdf = geopandas.GeoDataFrame(geometry=left_edge_points)
    if len(gdf) > 0:
        gdf.to_file(os.path.join(output_folder, "shapefiles", "left_edge_points.shp"))
        # or to Geojson file
        # gdf.to_file(os.path.join(output_folder, "shapefiles", "left_edge_points.geojason"), driver='GeoJSON')
option2:
    with fiona.open(os.path.join(output_folder, "shapefiles", "left_edge_line.shp")
            , 'w', 'ESRI Shapefile', {"geometry": "MultiLineString"}) as c:
        ## If there are multiple geometries, put the "for" loop here
        c.write({
            'geometry': mapping(complete_edges),
        })

```


#### Read shapefiles
``` 
import shapefile

def read_shape_file(shp_path):
    # -------------------------------------------------
    # Read the shapefiles
    # -------------------------------------------------
    with shapefile.Reader(shp_path) as shp:
        shp_data = list()
        for i in range(shp.numRecords):
            poly_3d = list()
            lines_x_y = shp.shape(i).points
            lines_z = shp.shape(i).z
            bbox = list(shp.shape(i).bbox)
            for num, item in enumerate(lines_x_y):
                poly_3d.append([item[0], item[1], lines_z[num]])

            #Create points in between before add to final result
            poly_3d = expand_points(poly_3d)
            shp_data.append([bbox, np.array(poly_3d, dtype=float)])

        shp_dataframe = pd.DataFrame(shp_data, columns=["bbox", "points"])

    return shp_dataframe

```

#### Write geojson 
``` 
import geojson

aa = geojson.Feature(geometry=geojson.Point((100, 100, 0)),properties={"class": "im here"})
bb = geojson.Feature(geometry=geojson.Point((200, 200, 500)),properties={"class": "there"})
feature_collection = geojson.FeatureCollection([aa,bb])

print(feature_collection)
# write to output file
with open("geodata.geojason", 'w') as f:
    geojson.dump(feature_collection, f)
```


#### Read dbf
``` 
from simpledbf import Dbf5
dbf = Dbf5(file_path)
df = dbf.to_dataframe()
```




# Scripts description
All handy scripts. Deciption of functions:
- [Folder To Subfolders](#Folder_to_subfolders)
- [read change json labels](#Read Change Json lables)


| name | short description | 
| --- | --- | 
| Folder_to_subfolders | split files in a folder into subfolders |



#### Folder_to_subfolders
Get the input dir and copy all files inside into output_dir and in different subfolders based on number of files you give as input
```More description:
You have a folder with large number of files that you want to split into some folders with fewer number of files in each
```
