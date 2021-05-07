'''
Data preprocessing for IS545 final project:
This python reads the merged crashes.csv from openrefine and creates new rows, including:
x(longitude), y(latitude), norm_x(normalized x), norm_y(normalized y).
It also drops duplicate rows and rows that do not have valid geometry data.
The resulted file is exported as clean_crashes.csv
'''
import pandas as pd

df = pd.read_csv('crashes.csv')
print("number of rows in the orgininal csv: ", df.shape[0])
df = df.drop_duplicates()
print("dropping duplicates: ", df.shape[0])
# splitting the geometry into x and y
df[['point','x','y']] = df.Geometry.str.split(expand=True)
df['x'] = df['x'].str.replace('(', '')
df['y'] = df['y'].str.replace(')', '')
# normalizing longitude and latitude
df = df.dropna(subset=['x', 'y'])
print("dropping null geometry: ", df.shape[0])
xMax = df["x"].astype(float).max()
xMin = df["x"].astype(float).min()
yMax = df["y"].astype(float).max()
yMin = df["y"].astype(float).min()
df["norm_x"] = (df["x"].astype(float) - xMin)/xMax
df["norm_x"] = 0-df["norm_x"]
df["norm_y"] = (df["y"].astype(float) - yMin)/yMax
# dropping useless columns
df = df.drop_duplicates()
df = df.drop(['point', 'Geometry'], 1)
print("number of rows in the output: ", df.shape[0])
df.to_csv (r'clean_crashes.csv', index = False, header=True)



