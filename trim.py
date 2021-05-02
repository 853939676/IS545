import pandas as pd

df = pd.read_csv('crashes.csv')
print(df.shape[0])
df = df.drop_duplicates()
print(df.shape[0])
df[['point','x','y']] = df.Geometry.str.split(expand=True)
df['x'] = df['x'].str.replace('(', '')
df['y'] = df['y'].str.replace(')', '')

df['crash_severity'] = df['crash_severity'].str.replace('PD', 'Property Damage')
df['city'] = df['city'].str.lower()
df['collision_type'] = df['collision_type'].str.lower()
df['weather'] = df['weather'].str.lower().replace(' / ', '/')
df['light'] = df['light'].str.lower().replace('unkown', 'unknown')
df['road_surface'] = df['road_surface'].str.lower().replace('unkown', 'unknown')
df['traffic_control'] = df['traffic_control'].str.lower().replace('unkown', 'unknown').replace(' / ', '/')
df.loc[(df['traffic_control'] == 'other regulatory sig')|(df['traffic_control'] == 'other reg. sign'),'traffic_control'] = 'other regulatory sign'

df = df.drop_duplicates()
print(df.shape[0])
df = df.drop(['point', 'Geometry'], 1)
df.to_csv (r'clean_crashes.csv', index = False, header=True)



