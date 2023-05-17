import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import geopandas as gpd
import plotly.express as px
import pyproj

app = dash.Dash(__name__)

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
    color_continuous_scale="turbo"
)

fig.update_geos(fitbounds="locations", visible=False)

app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.Div(
            children="""
   Dash: A web application framework for Python.
   """
        ),
        dcc.Graph(id="example-graph", figure=fig, style={"height": "100vh"}),
    ]
)


app.run_server(debug=True)

if __name__ == "__main__":
    app.run_server(debug=True)
