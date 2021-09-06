from keplergl import KeplerGl
import pandas as pd
import geopandas as gpd

df = pd.read_excel("ABCimages_namelist.xlsx", sheet_name='Sheet1')
map1 = KeplerGl(height=800)

# Create a geopandas dataframe from a regular dataframe
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.LON, df.LAT))
# Add data to Kepler
map1.add_data(data=gdf, name="test")

map1.save_to_html(file_name="test.html")

