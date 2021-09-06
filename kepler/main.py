from keplergl import KeplerGl
import pandas as pd
import geopandas as gpd
from datetime import datetime

df = pd.read_excel('ABCimages_namelist.xlsx', sheet_name='Sheet1')
map1 = KeplerGl(height=800)

df['CAMPAIGN_DATE'] = df.apply(lambda row: datetime.strptime(row['CAMPAIGN'][-6:],'%Y %b'), axis = 1)
df.to_csv('data.csv')
# Create a geopandas dataframe from a regular dataframe
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.LON, df.LAT))
# Add data to Kepler
map1.add_data(data=gdf, name="test")

map1.save_to_html(file_name="test.html")

