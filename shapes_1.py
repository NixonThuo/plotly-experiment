import geopandas as gpd
import plotly.express as px
import pyproj
import pandas as pd

geodf = gpd.read_file("kenya_shapes\County.shp")

geodf.to_crs(pyproj.CRS.from_epsg(4326), inplace=True)
df = pd.read_csv("kenya_data.csv")
"""
df_merged = geodf.merge(
    df, left_on=["COUNTY"], right_on=["COUNTY"]  # map_df merge to df
)
"""
df_merged = geodf.set_index("COUNTY").join(df.set_index("COUNTY"))

df_merged.head()

fig = px.choropleth(
    df_merged,
    geojson=df_merged.geometry,
    locations=df_merged.index,
    color="TREE-COVER",
)

fig.update_geos(fitbounds="locations", visible=False)
fig.show()
